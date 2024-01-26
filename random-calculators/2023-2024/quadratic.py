

# Python program to find roots of quadratic equation
import math 

from helper import sint
 
def parse_input(val):
    mapper = {"-": " -", "+": " "}
    new = ""
    for char in val:
        new += mapper.get(char, char)

    final = []
    for x in new.split(" "):
        if x not in ["", " "]:
            final.append(float(x))
    return final
 
# function for finding roots
def equation_roots( a, b, c): 
 
    # calculating discriminant using formula
    dis = (b ** 2) - (4 * a * c) 
    sqrt_val = math.sqrt(abs(dis)) 
     
    # checking condition for discriminant
    if dis > 0: 
        print("real and different roots:") 
        print(sint(-b + sqrt_val), "/" ,sint(2 * a)) 
        print(sint(-b - sqrt_val), "/" ,sint(2 * a)) 
        input("divide?")
        print(sint(-b + sqrt_val) / sint(2 * a)) 
        print(sint(-b - sqrt_val) / sint(2 * a)) 
     
    elif dis == 0: 
        print("real and same roots:") 
        print(sint(-b), "/", sint(2 * a)) 
        input("divide?")
        print(sint(-b) / sint(2 * a)) 
     
    # when discriminant is less than 0
    elif dis < 0:
        print("Complex Roots") 
        dis = sint(abs(dis))
        neg_b = sint(-b)
        two_a = sint(2 * a)
        print("(", neg_b, "+ i sqrt(", dis, ")", ") /", two_a) 
        print("(", neg_b, "- i sqrt(", dis, ") /", two_a) 
        
        input("simplify radical")
        coefficient, squared_rooted = simply_radical(int(dis))
        coefficient = sint(coefficient)
        squared_rooted = sint(squared_rooted)
        print("(", neg_b, "+", coefficient, "i sqrt(", squared_rooted, ")", ") /", two_a) 
        print("(", neg_b, "-", coefficient , "i sqrt(", squared_rooted, ") /", two_a)
        
        gcd = find_gcd(neg_b, coefficient, two_a)
        if gcd != 1:
            input("gcd")
            neg_b = sint(neg_b / gcd)
            coefficient = sint(coefficient / gcd)
            two_a = sint(two_a / gcd)
            print("(", neg_b, "+", coefficient, "i sqrt(", squared_rooted, ")", ") /", two_a) 
            print("(", neg_b, "-", coefficient , "i sqrt(", squared_rooted, ") /", two_a)
 
def simply_radical(num):
    for i in range(2, num):
        div, mod = divmod(num, i*i)
        if mod == 0:
            sq1, sq2 = simply_radical(div)
            return (i * sq1, sq2)
        if div == 0:
            break
    return (1, num)

def find_gcd(x, *nums):
    if len(nums) == 0:
        return x
    y, *new_nums = nums
    while y:
        x, y = y, x % y
    return abs(find_gcd(x, *new_nums))
 
while True:
    # Driver Program 
    a, b, c = parse_input(input("Enter equation: "))

    # If a is 0, then incorrect equation
    if a == 0: 
        print("Input correct quadratic equation") 
    else:
        equation_roots(a, b, c)
        
    print()