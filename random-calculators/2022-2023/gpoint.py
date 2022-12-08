from helper import get_sint, sint

while True:
    m = get_sint("m")
    b = get_sint("b")

    def print_X(y):
        print("x = %s, y = %s" % (sint((y - b) / m), y))

    def print_Y(x):
        print("x = %s, y = %s" % (x, sint(((m*x)+b)))) 

    print_X(0)
    print_Y(0)

    while True:
        v = input("val: ")
        if v in ["e", "exit", ""]:
            break

        vn = sint(eval(v[2:]))

        if v[:2] in ["x=", "X=", "X "]:
            print_Y(vn)
        elif v[:2] in ["y=", "Y=", "  "]:
            print_X(vn)
