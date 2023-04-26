from helper import get_sint

a = get_sint("a")
b = get_sint("b")
c = get_sint("c")

l = a ** 2 + b ** 2
r = c ** 2

if l < r:
    print("obtuse")
elif l > r:
    print("acute")
else:
    print("right")