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
    print("%s: (%s-%s)/(%s-%s) = %s" % (pre, p2[1], p1[1], p2[0], p1[0], a))
    return a

def dis(p1, p2, pre):
    a = sint(sqrt(sq(p2[0]-p1[0]) + sq(p2[1]-p2[1])))
    print("%s: sqrt(sq(%s-%s)+sq(%s-%s)) = %s" % (pre, p2[0], p1[0], p2[1], p2[1], a))
    return a


a = get_point("", "a")
b = get_point("", "b")
c = get_point("", "b")
d = get_point("", "d")
print()
ab_slp = slp(a, b, "ab")
bc_slp = slp(b, c, "bc")
cd_slp = slp(c, d, "cd")
da_slp = slp(d, a, "da")
input()
ab_dis = dis(a, b, "ab")
bc_dis = dis(b, c, "bc")
cd_dis = dis(c, d, "cd")
da_dis = dis(d, a, "da")
input()
# Rect Shape:
#  a - b
#  |   |
#  d - c

# Parallelogram: Opposite Sides are Congruent; Slopes of opposite sides do not make perpendicular lines
# Rhombus: All sides are Congruent; Slopes of opposite sides are congruent; they do not make perpendicular lines
# Rectangle: Opposite sides are Congruent; Slopes of opposite sides make perpendicular lines
# Square: All sides are Congruent; Slopes of opposite sides make perpendicular lines

is_para = False
is_rhom = False
is_rect = False
if ab_dis == cd_dis and da_dis == bc_dis:
    is_para = True
    if ab_dis == da_dis == cd_dis == bc_dis:
        is_rhom = True
    if (ab_slp * da_slp == -1 or (ab_slp == 0 and da_slp == float("NaN")) or (ab_slp == float("NaN") and da_slp == 0)) and (bc_slp * cd_slp == -1 or (bc_slp == 0 and cd_slp == float("NaN")) or (bc_slp == float("NaN") and cd_slp == 0)):
        is_rect = True

if is_rhom and is_rect:
    print("Square")
elif is_rhom:
    print("Rhombus")
elif is_rect:
    print("Rectangle")
elif is_para:
    print("Parallelogram")
else:
    print("Quadrilateral")