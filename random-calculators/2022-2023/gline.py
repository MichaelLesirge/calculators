from helper import get_point, get_sint, sint, simplify

while True:
    m = get_sint("m")

    x, y = get_point("", "p")

    mode = input("enter mode e/a/b: ")

    if mode == "b":
        parallel = True
        perpendicular = True
    elif mode == "a":
        parallel = True
        perpendicular = False
    elif mode == "e":
        parallel = False
        perpendicular = True

    if parallel:
        b = sint(y - (m * x))
        print("parallel: y = %sx + %s" % (m, b))
    if perpendicular:
        m = sint(-1 / m)
        b = y - (m * x)

        tb, bb = simplify(-1, m)
        print("b = %s/%s" % (tb, bb))
        print("perpendicular: y = %sx + %s" % (m, b))
    