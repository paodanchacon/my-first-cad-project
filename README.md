# Getting Started with build123d in Antigravity IDE

This guide documents the setup process for running `build123d` and visualizing your 3D models using the Antigravity IDE (which is based on VS Code/Open VSX).

## 1. Project Setup with `uv`

Instead of manually managing `pip` and virtual environments, we use `uv` for blazing fast dependency management.

1. Initialize a new Python project:
   ```bash
   uv init my_first_cad_project
   cd my_first_cad_project
   ```
2. Add the necessary CAD dependencies:
   ```bash
   uv add build123d ocp-vscode
   ```
   *(This automatically creates a hidden `.venv` virtual environment and installs the packages).*

## 2. Installing the OCP CAD Viewer

Because Antigravity IDE uses the Open VSX registry instead of the Microsoft Marketplace, you have to install the OCP CAD Viewer extension manually from a `.vsix` release.

1. Download the latest `ocp-cad-viewer.vsix` from the [official GitHub releases](https://github.com/bernhard-42/vscode-ocp-cad-viewer/releases). 
2. In Antigravity IDE, go to the **Extensions** sidebar (`Cmd+Shift+X`).
3. Click the **`...`** (More Actions) menu in the top right of the extensions pane.
4. Select **Install from VSIX...**
5. Locate the `.vsix` file you downloaded and select it.

## 3. Running Your Code

To see your 3D models, you must have the CAD Viewer open *before* you run your Python script.

1. Press **`Cmd+Shift+P`** to open the Command Palette.
2. Search for and select **`OCP CAD Viewer: Open viewer`**. A new pane will open to display your 3D models.
3. Switch back to your terminal, ensure you are in the project folder, and run your script using `uv`:
   ```bash
   uv run tutorials/hello_build123d.py
   # Or run main.py to see all available scripts:
   uv run main.py
   ```
   
Your model will instantly render in the viewer pane!

> **Note on VS Code Python Interpreters:** 
> If you want code autocompletion to work perfectly, you can tell VS Code to use your `uv` environment. Click on the Python version in the bottom right corner (or use `Python: Select Interpreter` in the Command Palette), select **Enter interpreter path... -> Find...**, press `Cmd+Shift+.` to show hidden files, and select the `.venv/bin/python` executable.

## 4. Understanding Your First CAD Design

The script (`tutorials/hello_build123d.py`) uses the **Builder Mode** paradigm. It leverages Python context managers (`with`) to keep track of active parts and sketches. 

Here is a breakdown of what the code does:

```python
from build123d import *
from ocp_vscode import show

# 1. Start a new part context. Everything built inside this block belongs to 'my_part'.
with BuildPart() as my_part:
    
    # 2. Create the base solid body: A rectangular prism (100x50x10 mm).
    Box(100, 50, 10)
    
    # 3. Select a face to sketch on. 
    # my_part.faces() gets all faces, sort_by(Axis.Z) sorts them by height, 
    # and [-1] grabs the very top one.
    with BuildSketch(my_part.faces().sort_by(Axis.Z)[-1]):
        # Draw a 2D circle with a radius of 15mm in the center of the face.
        Circle(15)
        
    # 4. Extrude the 2D sketch into a 3D operation.
    # A negative amount goes downwards into the box. 
    # Mode.SUBTRACT means we are cutting material away instead of adding it.
    extrude(amount=-10, mode=Mode.SUBTRACT)

# 5. Send the finished part to the OCP CAD Viewer pane in VS Code.
show(my_part)
```

## 5. Part 1 Breakdown (`tutorials/part1.py`)

For a deeper dive into a more complex design, including sketches, extrusions, fillets, and holes, check out the [tutorials/part1_explanation.md](tutorials/part1_explanation.md) guide.

It provides a step-by-step code breakdown and analysis of `tutorials/part1.py` (a U-shaped bracket) and includes suggested modifications to help you understand the parametric design workflow better!

## 6. Part 2 Breakdown (`tutorials/part2.py`)

For an example of 2D sketching with subtractive elements (a hexagon with a hole) and advanced topological edge selection for filleting, check out the [tutorials/part2_explanation.md](tutorials/part2_explanation.md) guide!

## 7. Project Structure

The repository is modularly organized into functional categories, each with its own documentation guide:

```text
my_first_cad_project/
├── main.py                         # Interactive CLI runner and directory index
├── pyproject.toml                  # Project metadata and dependencies
├── uv.lock                         # Pinned dependency lockfile
├── README.md                       # Main project setup and overview
│
├── tutorials/                      # Guided 3D parts & walkthroughs
│   ├── README.md                   # Detailed guide for all tutorials
│   ├── hello_build123d.py          # Basic solid body with subtractive cut
│   ├── flange_tutorial.py          # Parametric mounting flange with hole grid
│   ├── part1.py                    # Symmetric U-bracket model
│   ├── part1_explanation.md        # Mathematical & code breakdown of part 1
│   ├── part2.py                    # Hexagonal socket recess model
│   └── part2_explanation.md        # Topological selection breakdown of part 2
│
├── constraints/                    # 2D geometric constraints & line studies
│   ├── README.md                   # Comprehensive guide to constraint solvers
│   ├── triangle_constraints.py     # SSS, SAS, ASA, and right-angled solvers
│   ├── trapezoid_constraints.py    # Angle-constrained 4-sided trapezoids
│   ├── fillet_polyline.py          # 2D/3D polylines with variable corner fillets
│   ├── offset_constraint.py        # Wall offsets (Kind.ARC, INTERSECTION, TANGENT)
│   ├── blendcurve_constraint.py    # C1/C2 curvature continuity blending
│   └── tangency_constraint.py      # Apollonius circle tangency problem solver
│
└── assemblies/                     # Multi-body assemblies & joint connections
    ├── README.md                   # Guide to joint systems and mating
    └── joint_assembly.py           # RigidJoint mating of base and pin components
```

### Subfolder Documentation Guides
* 📖 [**`tutorials/README.md`**](tutorials/README.md) — Walkthroughs for modeling individual parts.
* 📐 [**`constraints/README.md`**](constraints/README.md) — In-depth reference for 2D constraint geometry and curves.
* 🔩 [**`assemblies/README.md`**](assemblies/README.md) — Reference for defining joints and mating parts.

Run `uv run main.py` in your terminal at any time to list all runnable scripts and execution commands.

