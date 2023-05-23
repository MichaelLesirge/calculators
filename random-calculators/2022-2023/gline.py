# get a parrel or perndicular line to slope on a point

from helper import get_point, get_sint, sint, simplify

while True:
    m = get_sint("m")

    x, y = get_point("", "p")


    b = sint(y - (m * x))
    print("parallel: y = %sx + %s" % (m, b))
    
    m = sint(-1 / m)
    b = y - (m * x)
    tb, bb = simplify(-1, m)
    print("b = %s/%s" % (tb, bb))
    print("perpendicular: y = %sx + %s" % (m, b))
    