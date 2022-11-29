from helper import sint


def slp(x1, y1, x2, y2):
    print("(%s - %s) / (%s - %s)" % (y2, y1, x2, x1))
    t, b = y2 - y1, x2 - x1
    print("%s / %s" % (t, b))
    try:
        s = t / b
    except ZeroDivisionError:
        s = "undifined"
    print(s)

    return s


while True:
    x1 = sint(input("x1: "))
    y1 = sint(input("y1: "))
    x2 = sint(input("x2: "))
    y2 = sint(input("y2: "))

    s = slp(x1, y1, x2, y2)
    print()
