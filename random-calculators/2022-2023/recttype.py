from helper import get_point, sint, gcd

def sq(x):
    return (x)**2

def sqrt(x):
    if x < 0:
        raise Exception("Can not square root negitive number %s" % x)
    return (x)**0.5

def slp(p1, p2, pre):
    try:
        a = sint((p2[1] - p1[1]) / (p2[0] - p1[0]))
    except ZeroDivisionError:
        a = float("NaN")
    print("%s: (%s - %s) / (%s - %s) = %s" % (pre, p2[1], p1[1], p2[0], p1[0], a))
    return a

def dis(p1, p2, pre):
    a = sint(sqrt(sq(p2[0]-p1[0]) + sq(p2[1]-p2[1])))
    print("%s: sqrt(sq(%s - %s) + sq(%s - %s)) = %s" % (pre, p2[0], p1[0], p2[1], p2[1], a))
    return a


a = get_point("", "a")
b = get_point("", "b")
c = get_point("", "b")
d = get_point("", "d")
print()
ab_slp = slp(a, b, "ab")
ad_slp = slp(a, d, "ad")
dc_slp = slp(d, c, "dc")
bc_slp = slp(b, c, "bc")
input()
ab_dis = dis(a, b, "ab")
ad_dis = dis(a, d, "ad")
dc_dis = dis(d, c, "dc")
bc_dis = dis(b, c, "bc")
input()
# Rect Shape:
#  a - b
#  |   |
#  d - c

# Parallelogram: Opposite Sides are Congruent; Slopes of opposite sides do not make perpendicular lines
# Rhombus: All sides are Congruent; Slopes of opposite sides are congruent; they do not make perpendicular lines
# Rectangle: Opposite sides are Congruent; Slopes of opposite sides make perpendicular lines
# Square: All sides are Congruent; Slopes of opposite sides make perpendicular lines

if ab_slp == dc_slp and ad_slp == bc_slp:
    if ab_dis == dc_dis and ad_dis == bc_dis:
        if ab_dis == ad_dis:
            print("Square")
        else:
            print("Rectangle")
    elif ab_dis == ad_dis and dc_dis == bc_dis:
        print("Rhombus")
    else:
        print("Parallelogram")
else:
    print("Quadrilateral")

