import cadquery as cq
import os

# Create a simple box
result = cq.Workplane("XY").box(10, 10, 10)

# Try exporting SVG
try:
    cq.exporters.export(
        result,
        "test_thumbnail.svg",
        opt={
            "width": 100,
            "height": 100,
            "marginLeft": 5,
            "marginTop": 5,
            "showAxes": False,
            "projectionDir": (1, 1, 1),
            "strokeWidth": 0.5,
            "strokeColor": (0, 0, 0),
            "hiddenColor": (100, 100, 100),
            "showHidden": True,
        },
    )
    print("SVG export successful")
except Exception as e:
    print(f"SVG export failed: {e}")
