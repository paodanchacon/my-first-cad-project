from build123d import geometry
from build123d import *
from ocp_vscode import show

with BuildPart() as my_part:
    Box(100,50,10)

    with BuildSketch(my_part.faces().sort_by(Axis.Z)[-1]):
        Circle(15)
    
    extrude(amount=-10, mode=Mode.SUBTRACT)
show(my_part)