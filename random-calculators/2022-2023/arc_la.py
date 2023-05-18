from helper import get_sint, sint
from math import pi

while True:
    r = get_sint("Radius")
    a = get_sint("Arc Angle")
    
    print("Lenght: ", sint((a * 2 * pi * r) / 360))
    print("Area: ", sint((a * pi * (r ** 2)) / 360))
    print()