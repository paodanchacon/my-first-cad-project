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
with BuildPart() as bracket:
    with BuildSketch(Plane.XY) as sketch:
        with BuildLine() as profile:
            FilletPolyline(
                (0, 0), (length/2, 0), (length/2, height), radius=bend_radius
            )
            offset(amount=thickness, side=Side.LEFT)
        make_face()
        mirror(about=Plane.YZ)
    extrude(amount=width / 2)
    mirror(about=Plane.XY)
    corners = bracket.edges().filter_by(Axis.X).group_by(Axis.Y)[-1]
    fillet(corners, fillet_radius)
    with Locations(bracket.faces().sort_by(Axis.X)[-1]):
        Hole(hole_diameter / 2)
    with BuildSketch(bracket.faces().sort_by(Axis.Y)[0]):
        SlotOverall(20 * MM, hole_diameter)
    extrude(amount=-thickness, mode=Mode.SUBTRACT)
show(bracket.part)