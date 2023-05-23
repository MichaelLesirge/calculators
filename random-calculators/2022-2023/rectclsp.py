# get what type of shape a Quadrilateral is from the 4 points

from helper import get_point, sint, simplify

def sq(x):
    return (x)**2

def sqrt(x):
    if x < 0:
        raise Exception("Can not square root negitive number %s" % x)
    return (x)**0.5

def slp(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    x, y = x2-x1, y2-y1
    try:
        m = y/x
        x, y = simplify(x,y)
    except ZeroDivisionError:
        m = float("NaN")
    print("(%s-%s)/(%s-%s) = %s/%s" % (y2, y1, x2, x1, sint(x), sint(y)))
    print("slp: %s" % (sint(m)))
    return m

def dis(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d = sq(x2-x1) + sq(y2-y1)
    ds = sqrt(d)
    print("sqrt(sq(%s-%s)+sq(%s-%s)) = sqrt(%s)" % (x2, x1, y2, y1, sint(d)))
    print("dis: %s" % (sint(ds)))
    return ds

al, bl, cl, dl = list((input("letters: ") or "abcd").upper())

a = get_point("", al)
b = get_point("", bl)
c = get_point("", cl)
d = get_point("", dl)
input(al+bl+": ")
ab_slp = slp(a, b)
ab_dis = dis(a, b)
input(bl+cl+": ")
bc_slp = slp(b, c)
bc_dis = dis(b, c)
input(cl+dl+": ")
cd_slp = slp(c, d)
cd_dis = dis(c, d)
input(dl+al+": ")
da_slp = slp(d, a)
da_dis = dis(d, a)
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