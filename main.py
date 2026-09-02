"""
Main entry point for build123d CAD studies and tutorials.
"""
import sys
from pathlib import Path


def list_scripts(category_dir: Path, title: str):
    print(f"\n📁 {title}:")
    scripts = sorted(category_dir.glob("*.py"))
    if not scripts:
        print("   (no scripts found)")
    for script in scripts:
        print(f"   • uv run {category_dir.name}/{script.name}")


def main():
    root = Path(__file__).parent
    print("=" * 60)
    print("🛠️  build123d CAD Learning & Experiments Hub")
    print("=" * 60)
    print("To visualize any part in VS Code:")
    print("1. Open OCP CAD Viewer pane (Cmd+Shift+P -> 'OCP CAD Viewer: Open viewer')")
    print("2. Run the desired script using uv:")

    list_scripts(root / "tutorials", "Tutorials & Parts")
    list_scripts(root / "constraints", "2D Constraint Studies")
    list_scripts(root / "assemblies", "Assemblies & Joints")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()

