import os
from geometry import GeometryAnalyzer

SAMPLES_DIR = "samples"


def verify():
    # Find a step file
    step_files = [
        f for f in os.listdir(SAMPLES_DIR) if f.endswith(".step") or f.endswith(".stp")
    ]
    if not step_files:
        print("No sample files found.")
        return

    sample_file = os.path.join(SAMPLES_DIR, step_files[0])
    print(f"Testing with {sample_file}...")

    try:
        analyzer = GeometryAnalyzer(sample_file)

        vol = analyzer.get_volume()
        print(f"Volume: {vol:.2f} cm^3")

        bbox = analyzer.get_bounding_box()
        print(f"Bounding Box: {bbox}")

        mass = analyzer.get_mass(2.7)  # Aluminum density
        print(f"Estimated Mass (Al): {mass:.2f} g")

        print("Geometry analysis verification passed!")

    except Exception as e:
        print(f"Verification failed: {e}")


if __name__ == "__main__":
    verify()
