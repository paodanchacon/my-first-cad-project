

from OCP import ShapeCustom
from OCP import APIHeaderSection
from ocp_vscode import show_object
from build123d import *
from ocp_vscode import *



with BuildLine() as path:
    line1 = Line((0,0),(30,0))
    line2 = Line((50,30),(80,30))
    blend = BlendCurve(
    curve0=line1,
    curve1=line2,
    continuity=ContinuityLevel.C1)

#show_object(line1)
#show_object(line2)
#show_object(path)
show_object(blend)