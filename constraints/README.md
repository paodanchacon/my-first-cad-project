# 2D Geometric Constraints & Line Operations

This directory contains experimental scripts exploring 2D sketch constraints, line constructions, curvature continuity, and offsets in `build123d`.

---

## Files Overview

| Script | Primary Classes / Methods | Key Concepts Explored |
| :--- | :--- | :--- |
| **[`triangle_constraints.py`](triangle_constraints.py)** | `Triangle(...)` | Geometric triangle solvers (SSS, SAS, ASA, Isosceles, Right-angle) solving angles and side lengths from partial constraints. |
| **[`trapezoid_constraints.py`](trapezoid_constraints.py)** | `Trapezoid(...)` | Symmetric, asymmetric, and right-angled trapezoids defined by width, height, and side angles. |
| **[`fillet_polyline.py`](fillet_polyline.py)** | `FilletPolyline(...)`, `BuildLine()` | 2D and 3D paths with rounded corners. Supports uniform radius, vertex-by-vertex variable radii, and open vs closed polylines. |
| **[`offset_constraint.py`](offset_constraint.py)** | `offset(...)`, `BuildSketch()` | Expanding or contracting 2D profiles with various corner transition algorithms (`Kind.ARC`, `Kind.INTERSECTION`, `Kind.TANGENT`). |
| **[`blendcurve_constraint.py`](blendcurve_constraint.py)** | `BlendCurve(...)`, `ContinuityLevel` | Smooth bridging transitions between disconnected curves with curvature continuity control ($C^0, C^1, C^2$). |
| **[`tangency_constraint.py`](tangency_constraint.py)** | `ConstrainedArcs(...)`, `Sagitta` | Apollonius circle problem solver: finding circles/arcs tangent to lines, circles, and passing through fixed points. |

---

## Detailed Script Breakdowns

### 1. `triangle_constraints.py`
Demonstrates `build123d`'s analytical triangle engine. You can fully constrain a triangle using classic geometric criteria:
* **Isosceles:** `Triangle(a=30, b=30, C=60)` — Two sides and included angle.
* **Right Angled:** `Triangle(a=30, c=30, B=90)` — Legs with a $90^\circ$ angle.
* **ASA (Angle-Side-Angle):** `Triangle(A=45, b=40, C=30)`.
* **SSS (Side-Side-Side):** `Triangle(a=30, b=40, c=50)`.
* **SAS (Side-Angle-Side):** `Triangle(a=30, B=45, c=30)`.

```bash
uv run constraints/triangle_constraints.py
```

---

### 2. `trapezoid_constraints.py`
Explores creating 4-sided trapezoids with angle constraints:
* **Right-Angled:** `Trapezoid(width=100, height=50, left_side_angle=90, right_side_angle=70)`
* **Symmetric:** `Trapezoid(width=60, height=30, left_side_angle=60, right_side_angle=60)`

```bash
uv run constraints/trapezoid_constraints.py
```

---

### 3. `fillet_polyline.py`
Demonstrates continuous path generation with automated corner rounding:
* **2D & 3D Paths:** Connects coordinates in 2D (`(x, y)`) or 3D (`(x, y, z)`), ideal for pipe routing or wiring harnesses.
* **Variable Fillets:** Pass an array of radii (e.g. `radii = [5, 15, 25, 10]`) to round each vertex by a different amount.
* **Open vs. Closed:** Set `close=True` for closed loops or `close=False` for open guide paths.

```bash
uv run constraints/fillet_polyline.py
```

---

### 4. `offset_constraint.py`
Demonstrates offsetting 2D sketches (used for creating wall thicknesses, clearances, or shells):
* **Corner Kinds:**
  * `Kind.ARC`: Rounds outer sharp corners by the offset radius.
  * `Kind.INTERSECTION`: Extends adjacent edges to sharp intersecting points.
  * `Kind.TANGENT`: Maintains smooth tangencies along curves.
* **Positive vs Negative:** Positive values expand the boundary outwards; negative values contract inward (making holes or internal clearances).

```bash
uv run constraints/offset_constraint.py
```

---

### 5. `blendcurve_constraint.py`
Demonstrates generating smooth blending curves between two non-intersecting lines or curves:
* **Parameters:** `curve0`, `curve1`, and `continuity`.
* **Continuity Levels:**
  * `ContinuityLevel.C1`: Tangency matching at junction points (no sudden directional kink).
  * `ContinuityLevel.C2`: Curvature matching (smooth acceleration, no optical seam).

```bash
uv run constraints/blendcurve_constraint.py
```

---

### 6. `tangency_constraint.py`
Explores the `ConstrainedArcs` builder for solving tangencies (Apollonius Problem):
* **Line-to-Line Fillets:** Creating arcs tangent to two reference edges.
* **Line-to-Point Arcs:** Creating arcs tangent to a line while passing through a specific coordinate point `(x, y)`.
* **Selectors & Sagitta:**
  * `sagitta=Sagitta.SHORT`: Minor arc ($\le 180^\circ$).
  * `sagitta=Sagitta.LONG`: Major arc ($> 180^\circ$).
  * `selector=lambda arcs: arcs[0]`: Selects candidate solution from multiple mathematical results.

```bash
uv run constraints/tangency_constraint.py
```
