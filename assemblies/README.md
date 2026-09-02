# Assemblies & Kinematic Joints

This directory explores multi-part assemblies, joint definitions, and mating in `build123d`.

---

## Files Overview

| Script | Primary Classes / Methods | Key Concepts Explored |
| :--- | :--- | :--- |
| **[`joint_assembly.py`](joint_assembly.py)** | `BuildPart()`, `RigidJoint(...)`, `connect_to(...)` | Creating multi-body parts, attaching local reference frame joints to faces, and mating them together. |

---

## Detailed Breakdown: `joint_assembly.py`

### 1. The Concept of Joints in `build123d`
Unlike basic modeling where parts are placed with absolute global coordinates, `build123d` provides **Joints** to define how components connect relative to each other:
* **`RigidJoint`**: Fully locks 6 degrees of freedom (translation and rotation).
* **`RevoluteJoint` / `LinearJoint`**: Allows rotational or translational motion for kinematic simulation.

### 2. How the Code Works
1. **Base Component:**
   * Creates a solid rectangular prism (`Box(60, 60, 10)`).
   * Defines a `RigidJoint` labeled `"top_mount"` centered on the top face (`Location((0, 0, 5))`).
2. **Pin Component:**
   * Creates a cylinder (`Cylinder(radius=10, height=30)`).
   * Defines a matching `RigidJoint` labeled `"bottom_mount"` centered on the bottom face (`Location((0, 0, -15))`).
3. **Mating:**
   * `base.joints["top_mount"].connect_to(pin.joints["bottom_mount"])` translates and rotates the pin so the two joint frames align perfectly.
4. **Visualization:**
   * Both bodies are passed to `show_object(...)` to inspect the assembly in the OCP CAD Viewer.

```bash
uv run assemblies/joint_assembly.py
```
