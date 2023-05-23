from math import sqrt

# random helper methods

def sint(x):
    x = float(x)
    if str(x)[-2:] == ".0" or x % 1 <= 0.00000000000001:
        return int(x)
    return x

def gcd(x, y):
	while y:
		x, y = y, x % y
	return abs(x)

def simplify(x, y):
  divisor = gcd(x, y)
  return (x / divisor, y / divisor)

def get_sint(prompt):
    return sint(eval(input(prompt + ": "), {"sqrt": sqrt}))

def get_point(point_num, prefix=""):
    return get_sint("%sx%s" % (prefix, point_num)), get_sint("%sy%s" % (prefix, point_num))