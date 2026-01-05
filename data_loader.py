"""
Data loader module for QuoteForge.
Fetches materials and processes data from Google Sheets CSV endpoints.
Implements time-based caching to reduce network requests.
"""

import json
import pandas as pd
from datetime import datetime, timedelta
from typing import Optional, Dict
import os

# In-memory cache
_cache: Dict[str, dict] = {}
_config: Optional[dict] = None


def load_config() -> dict:
    """Load configuration from config.json"""
    global _config
    if _config is None:
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as f:
            _config = json.load(f)
    return _config


def fetch_csv_data(url: str, cache_key: str) -> pd.DataFrame:
    """
    Fetch CSV data from URL with time-based caching.

    Args:
        url: URL to fetch CSV from
        cache_key: Key for caching this data

    Returns:
        DataFrame with CSV data
    """
    config = load_config()
    refresh_minutes = config.get("refresh_rate_minutes", 15)

    # Check cache
    if cache_key in _cache:
        cached_data = _cache[cache_key]
        cache_age = datetime.now() - cached_data["timestamp"]

        # Return cached data if fresh enough
        if cache_age < timedelta(minutes=refresh_minutes):
            print(f"[Data Loader] Using cached {cache_key} (age: {cache_age.seconds}s)")
            return cached_data["data"]

    # Fetch fresh data
    try:
        print(f"[Data Loader] Fetching fresh {cache_key} from Google Sheets...")
        df = pd.read_csv(url)

        # Update cache
        _cache[cache_key] = {"data": df, "timestamp": datetime.now()}

        print(f"[Data Loader] Successfully loaded {len(df)} {cache_key} rows")
        return df

    except Exception as e:
        # If fetch fails and we have cached data, return it
        if cache_key in _cache:
            print(f"[Data Loader] Fetch failed, using stale cached {cache_key}: {e}")
            return _cache[cache_key]["data"]
        else:
            print(f"[Data Loader] Fetch failed with no cache available: {e}")
            raise


def get_materials() -> pd.DataFrame:
    """Get materials data from Google Sheets"""
    config = load_config()
    url = config["endpoints"]["materials"]
    return fetch_csv_data(url, "materials")


def get_processes() -> pd.DataFrame:
    """Get processes data from Google Sheets"""
    config = load_config()
    url = config["endpoints"]["processes"]
    return fetch_csv_data(url, "processes")


def get_material_by_name(name: str) -> Optional[pd.Series]:
    """
    Get a specific material by name.

    Returns:
        Series with material data or None if not found
    """
    materials = get_materials()
    result = materials[materials["name"] == name]
    if len(result) > 0:
        return result.iloc[0]
    return None


def get_process_by_name(name: str) -> Optional[pd.Series]:
    """
    Get a specific process by name.

    Returns:
        Series with process data or None if not found
    """
    processes = get_processes()
    result = processes[processes["name"] == name]
    if len(result) > 0:
        return result.iloc[0]
    return None
