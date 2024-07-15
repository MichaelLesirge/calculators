from helper import get_sint, sint
from math import * 

while True:
    stop = get_sint("stop") + 1
    start = get_sint("start", 0)
    eq = input("equation: ")
    
    total_sum = 0
    for x in range(start, stop):
        total_sum += eval(eq, {"X": x, "x": x})
        
    print(sint(total_sum))
    print()