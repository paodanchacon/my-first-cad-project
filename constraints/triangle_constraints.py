

from OCP import ShapeCustom
from OCP import APIHeaderSection
from ocp_vscode import show_object
from build123d import *
from ocp_vscode import *
triangle_isosceles = Triangle(a=30, b=30, C=60)
triangle_right  = Triangle(a=30, c=30, B=90)
triangle_asa = Triangle(A=45, b=40, C=30)
triangle_sss = Triangle(a=30, b=40, c=50)
triangle_sas = Triangle(a=30, B=45, c=30)

#print(f"Side a: {triangle_isosceles.a}, 
#      f"Side b: {triangle_isosceles.b}, 
#      f"Side c: {triangle_isosceles.c}, 
#      f"Angle A: {triangle_isosceles.A}, 
#      f"Angle B: {triangle_isosceles.B}"
#.     f"Angle C: {triangle_isosceles.C})

#print(f"Side a: {triangle_right.a}", 
#      f"Side b: {triangle_right.b}", 
#      f"Side c: {triangle_right.c}",
#      f"Angle A: {triangle_right.A}", 
#      f"Angle B: {triangle_right.B}",
#      f"Angle C: {triangle_right.C}")

#print(f"Side a: {triangle_asa.a}", 
#      f"Side b: {triangle_asa.b}",
#      f"Side c: {triangle_asa.c}",
#      f"Angle A: {triangle_asa.A}",
#      f"Angle B: {triangle_asa.B}",
#      f"Angle C: {triangle_asa.C}")

#print(f"Side a: {triangle_sss.a}", 
#      f"Side b: {triangle_sss.b}",
#      f"Side c: {triangle_sss.c}",
#      f"Angle A: {triangle_sss.A}",
#      f"Angle B: {triangle_sss.B}",
#      f"Angle C: {triangle_sss.C}")

print(f"Side a: {triangle_sas.a}", 
      f"Side b: {triangle_sas.b}",
      f"Side c: {triangle_sas.c}",
      f"Angle A: {triangle_sas.A}",
      f"Angle B: {triangle_sas.B}",
      f"Angle C: {triangle_sas.C}")

#show_object(triangle_isosceles)
#show_object(triangle_right)
#show_object(triangle_asa)
#show_object(triangle_sss)
show_object(triangle_sas)
