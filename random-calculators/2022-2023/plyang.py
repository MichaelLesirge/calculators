# Get angle sums of polygon from numer of sides

from helper import get_sint, sint

while True:
    sides = get_sint("polygon sides")
    interior_angle_sum = (sides - 2) * 180
    print("Interior sum", sint(interior_angle_sum))
    print("Interior", sint(interior_angle_sum / sides))
    print("Exterior", sint(360 / sides))
    print()