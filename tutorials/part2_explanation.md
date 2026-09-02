# build123d Part 2 - Code Breakdown and Analysis

This document explains the `build123d` script in `part2.py`. The script creates a cylindrical base with a hex-shaped recess and a central hole, resembling a socket or the head of a specialized bolt.

## 1. Imports
```python
from build123d import *
from ocp_vscode import *
```
- We import everything from `build123d` for the CAD operations.
- We import everything from `ocp_vscode` (specifically `show`) to visualize the model in the IDE.

## 2. Base Cylinder
```python
with BuildPart() as example:
    Cylinder(radius=10, height=3)
```
- **`BuildPart`**: Starts the 3D part context named `example`.
- **`Cylinder`**: Creates a solid cylinder as the foundational body with a radius of 10 and a height of 3.

## 3. Sketching on a Face
```python
    with BuildSketch(example.faces().sort_by(Axis.Z)[-1]):
        RegularPolygon(radius=7, side_count=6)
        Circle(radius=4, mode=Mode.SUBTRACT)
```
- **`example.faces().sort_by(Axis.Z)[-1]`**: Selects the top face of the cylinder. It grabs all faces, sorts them by their Z (height) position, and takes the highest one (`[-1]`).
- **`BuildSketch`**: Initiates a 2D sketch on that top face.
- **`RegularPolygon`**: Draws a hexagon (`side_count=6`) with a radius of 7.
- **`Circle(..., mode=Mode.SUBTRACT)`**: Draws a circle in the center, but instead of adding to the sketch, it subtracts from the polygon shape. This creates a hexagonal sketch with a circular hole in the middle.

> [!TIP]
> **Suggested Change for Learning:** Try changing the `side_count` to 3 (triangle) or 4 (square). Alternatively, remove `mode=Mode.SUBTRACT` from the circle to see how overlapping shapes behave in a sketch.

## 4. Subtractive Extrusion
```python
    extrude(amount=-2, mode=Mode.SUBTRACT)
```
- **`extrude`**: Extrudes the sketch (hexagon with a hole) downwards by 2 units (`amount=-2`).
- **`mode=Mode.SUBTRACT`**: This cuts the extruded shape out of the original cylinder body, creating a recessed hex pocket and a deeper center hole.

## 5. Complex Edge Selection and Filleting
```python
    fillet(
        example.edges()
        .filter_by(GeomType.CIRCLE)
        .sort_by(SortBy.RADIUS)[-2:]
        .sort_by(Axis.Z)[-1],
        radius=1,
    )
```
This is a very specific edge selection sequence:
- **`example.edges()`**: Gets all edges in the current part.
- **`.filter_by(GeomType.CIRCLE)`**: Filters out straight edges (like the hex socket), keeping only circular edges (the outer rims and the central hole rims).
- **`.sort_by(SortBy.RADIUS)[-2:]`**: Sorts the remaining circular edges by their radius and keeps the two with the largest radius (`[-2:]`). This ignores the small central hole edges and focuses on the large outer cylinder rims.
- **`.sort_by(Axis.Z)[-1]`**: Of those two large rims, it sorts them by height (Z-axis) and grabs the highest one (`[-1]`). This isolates the top outer edge of the cylinder.
- **`fillet(..., radius=1)`**: Rounds that single selected edge with a radius of 1.

> [!TIP]
> **Suggested Change for Learning:** Edge selection can be tricky! Try changing `[-1]` to `[0]` in the `Axis.Z` sort to fillet the *bottom* edge instead. Or, change the radius sort to `[:2]` to target the small inner hole edges.

## 6. Visualization
```python
show(example.part)
```
- **`show`**: Renders the completed 3D part in the OCP CAD Viewer.
