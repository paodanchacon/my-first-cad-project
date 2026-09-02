from ezdxf import filemanagement
from ocp_vscode import show_object
from build123d import *
from ocp_vscode import *

# 2D square moving in x, y
points = [(0,0), (50,0), (50,50), (0,50)]
#with BuildLine() as path: 
    #FilletPolyline(*points, radius=10, close=False)
    #FilletPolyline(*points, radius=6, close=True)
    #FilletPolyline(*points, radius=25, close=True)

#show_object(path.line)

# 3D points moving in X, Y, and Z space
#points_3d = [(0, 0, 0), (50, 0, 0), (50, 50, 20), (0, 50, 50), (10,10,10)]

#with BuildLine() as path_3d:
    #FilletPolyline(*points_3d, radius=12, close=True)
    #FilletPolyline(*points_3d, radius=12, close=False)

#show_object(path_3d.line)


#points = [(0, 0), (80, 0), (80, 60), (0, 60)]
# Vertex 1 gets R=5, Vertex 2 gets R=15, Vertex 3 gets R=25, Vertex 4 gets R=10
#radii = [5, 15, 25, 10]

#with BuildLine() as path:
    #FilletPolyline(*points, radius=radii, close=True)

#show_object(path.line)


points_3d = [(0, 0, 0), (50, 0, 0), (50, 50, 20), (0, 50, 50)]

with BuildLine() as pipe_path:
    FilletPolyline(*points_3d, radius=12, close=False)

show_object(pipe_path.line)