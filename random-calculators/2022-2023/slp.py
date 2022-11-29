from helper import sint, gcd

def slp(x1, y1, x2, y2):
    print("(%s - %s) / (%s - %s)" % (y2, y1, x2, x1))
    t, b = sint(y2 - y1), sint(x2 - x1)
    print("(%s) / (%s)" % (t, b))
    try:
        s = sint(t / b)
    except ZeroDivisionError:
        s = "undifined"

    if t < 0 and b < 0:
        t, b = abs(t), abs(b)
    
    print("%s / %s" % (t, b))

    if isinstance(t, int) and isinstance(b, int):
        d = sint(gcd(abs(t), abs(b)))
        if d != 1:
            print("%s / %s gcd: %s" % (sint(t / d), sint(b / d), d))

    print(s)

    return s


while True:
    x1 = sint(input("x1: "))
    y1 = sint(input("y1: "))
    x2 = sint(input("x2: "))
    y2 = sint(input("y2: "))

    s = slp(x1, y1, x2, y2)
    print()
