# get what type of shape a Quadrilateral is from the 4 points

from helper import get_point, sint, gcd

def sq(x):
    return (x)**2

def sqrt(x):
    if x < 0:
        raise Exception("Can not square root negitive number %s" % x)
    return (x)**0.5

def slp(p1, p2, pre):
    x1, y1 = p1
    x2, y2 = p2
    try:
        m = sint((y2-y1)/(x2-x1))
    except ZeroDivisionError:
        m = float("NaN")
    print("%s: (%s-%s)/(%s-%s) = %s" % (pre, y2, y1, x2, x1, m))
    return m

def dis(p1, p2, pre):
    x1, y1 = p1
    x2, y2 = p2
    d = sint(sqrt(sq(x2-x1) + sq(y2-y1)))
    print("%s: sqrt(sq(%s-%s)+sq(%s-%s)) = %s" % (pre, x2, x1, y2, y1, d))
    return d

al, bl, cl, dl = list((input("letters: ") or "abcd").upper())

a = get_point("", al)
b = get_point("", bl)
c = get_point("", cl)
d = get_point("", dl)
print()
ab_slp = slp(a, b, al+bl)
bc_slp = slp(b, c, bl+cl)
cd_slp = slp(c, d, cl+dl)
da_slp = slp(d, a, dl+al)
input()
ab_dis = dis(a, b, al+bl)
bc_dis = dis(b, c, bl+cl)
cd_dis = dis(c, d, cl+dl)
da_dis = dis(d, a, dl+al)
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