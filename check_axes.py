import cadquery as cq  # type: ignore
import os

# Create a simple box
result = cq.Workplane("XY").box(10, 10, 10)

# Export SVG with axes
cq.exporters.export(
    result,
    "axes_test.svg",
    opt={
        "width": 100,
        "height": 100,
        "showAxes": True,
        "projectionDir": (1, 1, 1),
    },
)
print("Done")
