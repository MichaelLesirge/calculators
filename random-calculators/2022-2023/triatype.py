from helper import get_sint

while True:
    a = get_sint("a")
    b = get_sint("b")
    c = get_sint("c")

    l = a ** 2 + b ** 2
    r = c ** 2
    
    if c != max(a, b, c):
        print("C is not the highest value")        
    if not (a + b > c and a + c > b and b + c > a):
        print("Triangle is not valid")
    
    print()

    if l > r:
        print("%s^2 + %s^2 > %s^2" % (a, b, c))
        print("%s > %s" % (l, r))
        print("acute")
    elif l < r:
        print("%s^2 + %s^2 < %s^2" % (a, b, c))
        print("%s < %s" % (l, r))
        print("obtuse")
    else:
        print("%s^2 + %s^2 = %s^2" % (a, b, c))
        print("%s = %s" % (l, r))
        print("right")
    print()