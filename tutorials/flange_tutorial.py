from build123d import *
from ocp_vscode import show

# --- Parametric Variables ---
# Changing these numbers will automatically update the whole model!
flange_width = 80
flange_thickness = 10
center_hole_dia = 20
hole_edge_offset = 20  # 1cm (10mm) from the edge!
bolt_hole_dia = 10

with BuildPart() as flange:
    # 1. Create the base block
    Box(flange_width, flange_width, flange_thickness)
    
    # 2. Fillet (round) the 4 outer vertical corners.
    fillet(flange.edges().filter_by(Axis.Z), radius=10)
    
    # 3. Create the large central hole
    with BuildSketch(flange.faces().sort_by(Axis.Z)[-1]):
        Circle(center_hole_dia / 2)
    extrude(amount=-flange_thickness, mode=Mode.SUBTRACT)
    
    # 4. Create mounting holes based on distance from the edge
    with BuildSketch(flange.faces().sort_by(Axis.Z)[-1]):
        # GridLocations creates a square pattern!
        # The spacing between holes is the total width minus the offsets on BOTH sides.
        hole_spacing = flange_width - (hole_edge_offset * 2)
        with GridLocations(x_spacing=hole_spacing, y_spacing=hole_spacing, x_count=2, y_count=2):
            Circle(bolt_hole_dia / 2)
            
    # Extrude all 4 bolt holes downwards through the part
    extrude(amount=-flange_thickness, mode=Mode.SUBTRACT)

# Show the finished part in the CAD Viewer
show(flange, names=["Parametric_Flange"])
