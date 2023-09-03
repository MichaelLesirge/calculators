from algebraic_expression import Expression
import multiprocessing
from math import floor, ceil

"""Mostly made just to learn multithreading in python, not meant to be useful. No real error handling"""

leave_keywords = {"ex", "exit", "leave", "quit", "get me out of here!!!!!"}

def type_input(type, prompt = "", default = None, *, end = ": "):
    return type(input(prompt + f" (default {default})" + end) or default)

def find_value(expression: Expression, answer: int, min_possible: int, max_possible: int, num_of_decimals: int):
    answer = round(answer, num_of_decimals)
    for i in range(min_possible, max_possible):
        if round(expression.set_equal(i), num_of_decimals) == answer:
            return i

def stared_find_value(args):
    return find_value(*args)

def main() -> None:
    print("Welcome to brute force algebraic expression solver.")
    print("Use to determine what number makes left side of equation work single variable expressions")
    print()
    print("Example Input: x^2 + 2 = 27")
    print("Example Output: x = 5")
    print()
    print("Please be specific on the following questions to avoid unnecessarily longer run time.")

    cpu_count = multiprocessing.cpu_count()
    
    going = True

    while going:
        print()
        user_input = input("Enter equation: ")
        
        if user_input in leave_keywords:
            print("Bye Bye")
            exit(0)
            
        expression, answer = user_input.split("=")
        expression = Expression(expression)
        answer = float(answer)
        
        min_possible = type_input(float, "What is the minimum possible number it could be", -1000)
        max_possible = type_input(float, "What is the maximum number it could be", 1000)
        num_of_decimals = type_input(int, "How many decimals places", 0)
    
        confirm = input(f"Warning: this program will use all {cpu_count} of your cores. Start (Y/n): ").lower().strip()
        
        if confirm == "n":
            print("Cancelling...")
            continue
        
        chunk_size = ceil((max_possible - min_possible) / cpu_count)
        
        expression_var_value = None
        
        with multiprocessing.Pool(cpu_count) as pool:
            outputs = pool.imap_unordered(stared_find_value, [(expression, answer, start_val, start_val + chunk_size, num_of_decimals) for start_val in range(floor(min_possible), ceil(max_possible), chunk_size)])
            
            while expression_var_value is None:
                expression_var_value = next(outputs, "No valid value found")
            
            pool.terminate()

        print(expression_var_value)

if __name__ == "__main__":
    main()
