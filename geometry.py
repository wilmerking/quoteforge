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
        """Returns volume in cubic inches (assuming file is in mm)"""
        # 1 cubic inch = 16387.064 mm^3
        if self.shape:
            return self.shape.val().Volume() / 16387.064
        return 0.0

    def get_bounding_box(self):
        """Returns (dx, dy, dz) in inches (assuming file is in mm)"""
        if self.shape:
            bb = self.shape.val().BoundingBox()
            return (bb.xlen / 25.4, bb.ylen / 25.4, bb.zlen / 25.4)
        return (0.0, 0.0, 0.0)

    def get_surface_area(self):
        """Returns surface area in square inches (assuming file is in mm)"""
        # 1 square inch = 645.16 mm^2
        if self.shape:
            return self.shape.val().Area() / 645.16
        return 0.0

    def get_mass(self, density_lbs_in3):
        """Returns mass in lbs"""
        volume_in3 = self.get_volume()
        return volume_in3 * density_lbs_in3

    def export_stl(self):
        """Exports to a temporary STL file for visualization"""
        if self.shape:
            with tempfile.NamedTemporaryFile(suffix=".stl", delete=False) as tmp:
                cq.exporters.export(self.shape, tmp.name)
                return tmp.name
        return None

    def get_thumbnail_svg(self):
        """Generates an SVG thumbnail and returns the content as a string"""
        if self.shape:
            with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as tmp:
                cq.exporters.export(
                    self.shape,
                    tmp.name,
                    opt={
                        "width": 200,
                        "height": 200,
                        "marginLeft": 5,
                        "marginTop": 5,
                        "showAxes": False,
                        "projectionDir": (1, 1, 1),
                        "strokeWidth": 0.5,
                        "strokeColor": (255, 255, 255),
                        "hiddenColor": (150, 150, 150),
                        "showHidden": False,
                    },
                )
                tmp.close()
                with open(tmp.name, "r") as f:
                    svg_content = f.read()
                os.unlink(tmp.name)
                return svg_content
        return None
