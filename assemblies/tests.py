from build123d import *
from ocp_vscode import *

with BuildPart() as bp:
    with BuildSketch() as bs:
        # width = total outer length, height = total outer height (circle diameter)
        SlotOverall(width=70, height=40, rotation=0)
    extrude(amount=20)

result = bp.part
show(result)