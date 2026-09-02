# Tutorials & Guided CAD Parts

This directory contains foundational 3D modeling tutorials using `build123d`, progressing from basic subtractive sketches to complex parametric parts and filleted profiles.

---

## Files Overview

| Tutorial / Part | Companion Guide | Key Concepts Explored |
| :--- | :--- | :--- |
| **[`hello_build123d.py`](hello_build123d.py)** | Embedded in main README | `BuildPart`, `Box`, `BuildSketch` on a selected face, `Circle`, subtractive `extrude`. |
| **[`flange_tutorial.py`](flange_tutorial.py)** | Inline documented | Fully parametric mounting flange, edge filtering with `edges().filter_by(Axis.Z)`, corner filleting, and `GridLocations` pattern for bolt holes. |
| **[`part1.py`](part1.py)** | **[`part1_explanation.md`](part1_explanation.md)** | Symmetric U-bracket with outer bend radius, variable wall thickness, mounting holes, and rounded slot profiles. |
| **[`part2.py`](part2.py)** | **[`part2_explanation.md`](part2_explanation.md)** | Cylindrical socket base with subtractive hexagonal recess (`RegularPolygon`), center bore, and topological edge selection for chamfers/fillets. |

---

## Running the Tutorials

From the project root:

```bash
# 1. First CAD part
uv run tutorials/hello_build123d.py

# 2. Parametric Flange
uv run tutorials/flange_tutorial.py

# 3. U-Bracket (Part 1)
uv run tutorials/part1.py

# 4. Hex Socket Head (Part 2)
uv run tutorials/part2.py
```

Check [part1_explanation.md](part1_explanation.md) and [part2_explanation.md](part2_explanation.md) for deep-dive mathematical and topological analyses of those models.
