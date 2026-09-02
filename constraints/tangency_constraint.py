from ezdxf.colors import BLACK
from ezdxf.colors import GREEN
from ezdxf.colors import BLUE
from ocp_vscode import show_object
from build123d import *


with BuildLine() as path:
    line1 = Line((0,0),(50,0))
    #line2 = Line((50,0),(50,50))
    point = (25,50)
    arc = ConstrainedArcs(
        line1,
        #line2,
        point,
        radius=30,
        sagitta=Sagitta.SHORT,
        selector=lambda arcs: arcs[0],
        #mode=Mode.PRIVATE
    )
#show_object(line1)
#show_object(line2)
show_object(line1, name="ref_line1", options={"color": (255,0,0)})
#show_object(line2, name="ref_line2", options={"color": (255,0,0)})
show_object(arc, name="arc", options={"color": (0,255,0)})
show_object(point, name="point", options={"color": (0,0,255)})
show_object(Vertex(point), name="target_pt", options={"color": (0, 0, 255)})

#show_object(path)