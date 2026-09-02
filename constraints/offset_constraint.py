from ocp_vscode import show_object
from build123d import *
from ocp_vscode import *

with BuildSketch() as sketch: 
    r = Rectangle(40,20)
    #t = Trapezoid(width=40, height=20,left_side_angle=60, right_side_angle=70)
    #offset(amount=5, kind=Kind.ARC)
    #offset(amount=10, kind=Kind.ARC)
    #offset(amount=5, kind=Kind.INTERSECTION)
    #offset(amount=-5, kind=Kind.INTERSECTION)
    offset(amount=5, kind=Kind.TANGENT)

show_object(sketch.sketch)
    