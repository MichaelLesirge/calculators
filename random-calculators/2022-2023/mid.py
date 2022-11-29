from helper import sint


def mid(x1, y1, x2, y2):
    print("((%s + %s) / 2, (%s + %s) / 2)" % (x2, x1, y2, y1))
    x, y = sint(x2 + x1), sint(y2 + y1)
    print("(%s / 2, %s / 2)" % (x, y))
    x, y = sint(x / 2), sint(x / 2)
    print("(%s, %s)" % (x, y))
    return x, y


while True:
    x1 = sint(input("x1: "))
    y1 = sint(input("y1: "))
    x2 = sint(input("x2: "))
    y2 = sint(input("y2: "))

    m = mid(x1, y1, x2, y2)
    print()
