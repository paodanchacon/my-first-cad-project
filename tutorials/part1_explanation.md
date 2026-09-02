# build123d Part 1 - Code Breakdown and Analysis

This document explains the `build123d` script in `part1.py` step-by-step. The design is a symmetric U-shaped bracket with holes and a slot. 

## 1. Imports and Parameters
```python
from build123d import geometry
from build123d import *
from ocp_vscode import show

length = 60
height = 30
bend_radius = 9
thickness = 6
fillet_radius = 3
width = 30
hole_diameter = 6
```
> [!NOTE]
> The parameters define the overall dimensions of our bracket. Changing these allows us to easily scale and adjust the design without modifying the core logic.

## 2. Sketching the Profile
```python
with BuildPart() as bracket:
    with BuildSketch(Plane.XY) as sketch:
        with BuildLine() as profile:
            FilletPolyline(
                (0, 0), (length/2, 0), (length/2, height), radius=bend_radius
            )
            offset(amount=thickness, side=Side.LEFT)
        make_face()
        mirror(about=Plane.YZ)
```
- **`BuildPart`**: Starts the main 3D part context.
- **`BuildSketch`**: Creates a 2D sketch on the XY plane.
- **`BuildLine`**: Begins a line/path drawing sequence.
- **`FilletPolyline`**: Draws a line from the origin `(0, 0)` horizontally to `(length/2, 0)`, and then vertically to `(length/2, height)`. The `radius=bend_radius` automatically creates a rounded corner (bend) at the intersection. 
- **`offset`**: Thickens the line to create a closed shape. 
- **`make_face()`**: Converts the closed lines into a solid 2D face.
- **`mirror(about=Plane.YZ)`**: Mirrors the half-profile across the YZ plane to create a complete U-shape. 

> [!TIP]
> **Suggested Change for Learning:** Try modifying `Side.LEFT` to `Side.RIGHT` or `Side.BOTH` in the `offset` operation. How does this affect the final width or internal dimensions of the U-shape?

## 3. Extrusion and Mirroring
```python
    extrude(amount=width / 2)
    mirror(about=Plane.XY)
```
- **`extrude`**: Pulls the 2D face into a 3D solid by half the target width. 
- **`mirror(about=Plane.XY)`**: Mirrors the extruded half to create the full width, making the part symmetric around the XY plane.

## 4. Edge Fillets
```python
    corners = bracket.edges().filter_by(Axis.X).group_by(Axis.Y)[-1]
    fillet(corners, fillet_radius)
```
- **`filter_by(Axis.X)`**: Selects edges that run parallel to the X-axis.
- **`group_by(Axis.Y)[-1]`**: Groups those selected edges by their position along the Y-axis and selects the group furthest away (`[-1]`), which corresponds to the top outer edges of the U-shape.
- **`fillet`**: Rounds the selected edges.

> [!TIP]
> **Suggested Change for Learning:** Try changing `[-1]` to `[0]` to see which edges are selected instead. Also, try filtering by `Axis.Z` or grouping by `Axis.Z` to practice targeting different corners (like the internal ones).

## 5. Adding Holes
```python
    with Locations(bracket.faces().sort_by(Axis.X)[-1]):
        Hole(hole_diameter / 2)
```
- **`sort_by(Axis.X)[-1]`**: Finds the face furthest along the X-axis (the right outer face).
- **`Locations`**: Sets the context to the center of this selected face.
- **`Hole`**: Drills a hole through the part at that location.

## 6. Adding a Slot
```python
    with BuildSketch(bracket.faces().sort_by(Axis.Y)[0]):
        SlotOverall(20 * MM, hole_diameter)
    extrude(amount=-thickness, mode=Mode.SUBTRACT)
```
- **`sort_by(Axis.Y)[0]`**: Finds the face at the lowest Y position (the bottom outer face).
- **`BuildSketch`**: Starts a new sketch on this face.
- **`SlotOverall`**: Draws a slot shape.
- **`extrude(... mode=Mode.SUBTRACT)`**: Extrudes the slot shape negatively into the part to cut out the material.

> [!TIP]
> **Suggested Change for Learning:** The design is mirrored earlier, but only one hole is added to the right side. If you want holes on both sides, try moving the `Hole` operation *before* the final mirroring step, or use `mirror()` on the hole feature itself!

## 7. Displaying the Result
```python
show(bracket.part)
```
- **`show`**: Uses the `ocp_vscode` viewer to render the final `build123d` part.
