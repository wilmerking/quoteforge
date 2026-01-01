try:
    import cadquery as cq
except ImportError as e:
    import sys

    print(f"DEBUG: Failed to import cadquery in geometry.py: {e}")
    print(f"DEBUG: sys.path: {sys.path}")
    raise e
import tempfile
import os
import trimesh


class GeometryAnalyzer:
    def __init__(self, step_file_path):
        self.file_path = step_file_path
        self.shape = None
        self._load_file()

    def _load_file(self):
        try:
            self.shape = cq.importers.importStep(self.file_path)
        except Exception as e:
            raise ValueError(f"Failed to load STEP file: {e}")

    def get_volume(self):
        """Returns volume in cm^3 (assuming file is in mm, converts to cm^3)"""
        # CadQuery usually works in mm. Volume is mm^3.
        # 1 cm^3 = 1000 mm^3
        if self.shape:
            return self.shape.val().Volume() / 1000.0
        return 0.0

    def get_bounding_box(self):
        """Returns (dx, dy, dz) in mm"""
        if self.shape:
            bb = self.shape.val().BoundingBox()
            return (bb.xlen, bb.ylen, bb.zlen)
        return (0.0, 0.0, 0.0)

    def get_surface_area(self):
        """Returns surface area in cm^2"""
        if self.shape:
            return self.shape.val().Area() / 100.0
        return 0.0

    def get_mass(self, density_g_cm3):
        """Returns mass in grams"""
        volume_cm3 = self.get_volume()
        return volume_cm3 * density_g_cm3

    def export_stl(self):
        """Exports to a temporary STL file for visualization"""
        if self.shape:
            with tempfile.NamedTemporaryFile(suffix=".stl", delete=False) as tmp:
                cq.exporters.export(self.shape, tmp.name)
                return tmp.name
        return None
