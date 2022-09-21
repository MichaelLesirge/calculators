while True:
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    print("((%s + %s) / 2, (%s + %s) / 2)" % (x1, x2, y1, y2))
    print("(%s / 2, %s / 2)" % (x1 + x2, y1 + y2))
    print("(%s, %s)" % ((x1 + x2)/2, (y1 + y2)/2))
    print()