def sint(x):
    x = float(x)
    if str(x)[-2:] == ".0":
        return int(x)
    return x

while True:
    x1 = sint(input("x1: "))
    y1 = sint(input("y1: "))
    x2 = sint(input("x2: "))
    y2 = sint(input("y2: "))

    print("((%s + %s) / 2, (%s + %s) / 2)" % (x1, x2, y1, y2))
    x, y = sint(x1 + x2), sint(y1 + y2)
    print("(%s / 2, %s / 2)" % (x, y))
    x, y = sint(x / 2), sint(x / 2) 
    print("(%s, %s)" % (x, y))
    print()