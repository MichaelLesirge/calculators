from helper import get_sint, sint, gcd, simplify

def s(x):
    return (sint(x[0]), sint(x[2]))

while True:
    a1 = get_sint("a1")
    b1 = get_sint("b1")
    c1 = get_sint("c1")
    
    a2 = get_sint("a2")
    b2 = get_sint("b2")
    c2 = get_sint("c2")

    ra = s(simplify(a1, a2))
    print("a: %s:%s -> %s:%s (%s) " % (a1, a2, *ra, gcd(a1, a2)))
    rb = s(simplify(b1, b2))
    print("b: %s:%s -> %s:%s (%s) " % (b1, b2, *rb, gcd(b1, b2)))
    rc = s(simplify(c1, c2))
    print("c: %s:%s -> %s:%s (%s) " % (c1, a2, *ra, gcd(a1, a2)))
    
    if ra == rb == rc:
        print("simarlar %s:%s" % ra)
    else:
        print("not simalar")

