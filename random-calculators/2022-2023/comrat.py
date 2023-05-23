# get if 2 triangles have similar ratios

from helper import get_sint, sint, gcd, simplify

def s(x):
    return (sint(x[0]), sint(x[1]))

while True:
    vs = []
    for c in "abc":
        v1 = get_sint(c + "1")
        v2 = get_sint(c + "2")
        
        r = s(simplify(v1, v2))
        
        vs.append(r)
    
        print("%s: %s:%s -> %s:%s (%s) " % (c, v1, v2, *r, gcd(v1, v2)))

    if vs[0] == vs[1] == vs[2]:
        print("simarlar %s:%s" % vs[0])
    else:
        print("not simalar")

