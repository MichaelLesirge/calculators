from helper import get_sint, sint
from math import pi



while True:
    radius = get_sint("Radius")
    ark_angle = get_sint("Arc Angle")
    
    lenght = sint((ark_angle * 2 * pi * radius) / 360)
    print("len / (2 * pi * %s) = %s / 360" % (radius, ark_angle))
    print("Lenght: ", lenght)
    
    print("area / (pi * %s^2) = %s / 360" % (radius, ark_angle))
    area = sint((ark_angle * pi * (radius ** 2)) / 360)
    print("Area: ", area)
    print()

