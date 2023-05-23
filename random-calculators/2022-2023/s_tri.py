# get distances between triangle points

from helper import sint, get_point

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
    ax, ay = get_point("A")
    bx, by = get_point("B")
    cx, cy = get_point("C")

    print("AB =", dis(ax, ay, bx, by))
    print("BC =", dis(bx, by, cx, cy))
    print("AC =", dis(ax, ay, cx, cy))
