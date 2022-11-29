from helper import sint


def sq(x):
    return (x)**2


def sqrt(x):
    if x < 0:
        raise Exception("Can not square root negitive number %s" % x)
    return (x)**0.5


def dis(x1, y1, x2, y2):
    print("sqrt(sq(%s - %s) + sq(%s - %s))" % (x2, x1, y2, y1))
    x, y = sint(x2-x1), sint(y2-y1)
    print("sqrt(sq(%s) + sq(%s))" % (x, y))
    x, y = sint(sq(x1-x2)), sint(sq(y1-y2))
    print("sqrt(%s + %s)" % (x, y))
    a = sint(x + y)
    print("sqrt(%s)" % (a))
    a = sint(sqrt(a))
    print(a)


while True:
    x1 = sint(input("x1: "))
    y1 = sint(input("y1: "))
    x2 = sint(input("x2: "))
    y2 = sint(input("y2: "))

    d = dis(x1, y1, x2, y2)
    print()
