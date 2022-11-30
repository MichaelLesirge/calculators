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

    try:
        if isinstance(t, int) and isinstance(b, int):
            d = sint(gcd(abs(t), abs(b)))
            if d != 1:
                print("%s / %s gcd: %s" % (sint(t / d), sint(b / d), d))
    except ZeroDivisionError:
        pass

    print(s)

    return s

def mkycep(x1, y1, x2, y2):
    m = slp(x1, y1, x2, y2)

    print("m = %s" % m)

    input()

    print("(%s) = %s(%s) + b" % (y1, m, x1))
    lq = sint(m * x1)
    print("%s = %s + b" % (y1, lq))
    b = sint(y1 - lq)
    print("%s = b" % b)

    input()

    print("m = %s" % m)
    print("b = %s" % b)
    print("y = %sx + %s" % (m, b))


while True:
    x1 = sint(input("x1: "))
    y1 = sint(input("y1: "))
    x2 = sint(input("x2: "))
    y2 = sint(input("y2: "))

    s = mkycep(x1, y1, x2, y2)
    print()
