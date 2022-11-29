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
    