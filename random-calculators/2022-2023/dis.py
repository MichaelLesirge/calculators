def sq(x):
    return (x)**2

def sqrt(x):
    if x < 0:
        raise Exception("Can not square root negitive number %s" % x)
    return (x)**0.5

while True:
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    print("sqrt(sq(%s - %s) + sq(%s - %s))" % (x1, x2, y1, y2))
    print("sqrt(sq(%s) + sq(%s))" % (x1-x2, y1-y2))
    print("sqrt(%s + %s)" % (sq(x1-x2), sq(y1-y2)))
    print("sqrt(%s)" % (sq(x1-x2) + sq(y1-y2)))
    print("%s" % sqrt(sq(x1-x2) + sq(y1-y2)))
    print()