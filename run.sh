#!/bin/bash
# QuoteForge startup script
# This ensures we use the correct Python environment with all dependencies

# Install dependencies
/opt/homebrew/Caskroom/miniconda/base/bin/python -m pip install -r requirements.txt
/opt/homebrew/Caskroom/miniconda/base/bin/python -m pip install svglib --no-deps

# Run the app
/opt/homebrew/Caskroom/miniconda/base/bin/python -m streamlit run app.py
