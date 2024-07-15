from math import *

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

NO_DEFAULT = object()
def get_sint(prompt, default = NO_DEFAULT):
    # i know its bad
    value = input(prompt + ("" if default == NO_DEFAULT else " (default %s)" % default) + ": ")
    if (value == "" and default != NO_DEFAULT): value = repr(default)
    return sint(eval(value))

def get_point(point_num, prefix=""):
    return get_sint("%sx%s" % (prefix, point_num)), get_sint("%sy%s" % (prefix, point_num))