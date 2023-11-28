import multiprocessing
from math import sqrt
import itertools
import functools

"""
Brute force for the win! I payed for all 12 cores, and I am going to use them!
At some point I will go back and remake this using a smarter solution (JK).

This is probably some of the worst code I have ever written
"""

sqrt = functools.cache(sqrt)

class Config:
    NUM_RANGE = range(1, 21)
    NUMS = [6, 8, 3, 5]

    # BINARY_OPS = ["+", "-", "*", "/", "**"]
    # UNARY_OPS = ["%s", "-%s", "sqrt(%s)", "-sqrt(%s)"]
    BINARY_OPS = ["+", "-", "*", "/"]
    UNARY_OPS = ["%s", "-%s"]

import itertools

def make_parentheses_template(n: int) -> list[str]:
    if n == 4: return ["0+0+0+0", "(0+0)+0+0", "0+(0+0)+0", "0+0+(0+0)", "(0+0)+(0+0)", "(0+0+0)+0", "((0+0)+0)+0", "(0+(0+0))+0", "0+(0+0+0)", "0+((0+0)+0)", "0+(0+(0+0))",]
    return "+".join(["0"] * n)
    
def find_sum(data_set: list[str], binary_ops_products) -> dict[str, int]: 
    valid_nums = {}
    to_find = 0
    for op_set in binary_ops_products:
        eval_str = op_set % data_set
        try:
            output = eval(eval_str)
        except (OverflowError, ZeroDivisionError):
            pass
        else:
            if isinstance(output, (float, int)) and output in Config.NUM_RANGE:
                eval_str = eval_str.replace("- -", "+ ").replace("- +", "- ").replace("+ -", "- ")
                output = int(output)
                # print(f"{eval_str} = {output}")
                valid_nums[eval_str] = output
                to_find += 1
                if to_find == len(Config.NUM_RANGE): return valid_nums
    return valid_nums

def main() -> None:    
    parens_products = make_parentheses_template(len(Config.NUMS))
    
    
    binary_ops_products = []
    for paren in parens_products:
        binary_ops_products.extend([(paren.replace("+", " %s ") % p).replace("0", "%s") for p in itertools.product(Config.BINARY_OPS, repeat = len(Config.NUMS) - 1)])
    unary_ops_products = list(itertools.product(Config.UNARY_OPS, repeat = len(Config.NUMS)))
    
    num_permutations: list[list[str]] = []
    for num_set in itertools.permutations(Config.NUMS):
        for op_set in unary_ops_products:
            num_permutations.append(tuple(op % num for op, num in zip(op_set, num_set)))
    
    # print(num_permutations)    
    
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        func = functools.partial(find_sum, binary_ops_products=binary_ops_products)
        results = pool.imap_unordered(func, [perm for perm in num_permutations])
        
        answers: dict[int, set] = {}
        done_count = 0
        for result in results:
            for solution, num in result.items():
                if num not in answers:
                    done_count += 1
                    print(f"{done_count / len(Config.NUM_RANGE):.0%}: {solution} = {num}")
                answers.setdefault(num, set()).add(solution)
        
        print("\nBest solutions: ")
        
        for num in Config.NUM_RANGE:
            all_solutions = answers.get(num)
            
            if all_solutions is None:
                print(f"No answers for {num}")
            else:     
                best_solution = min(all_solutions, key = len)
                print(f"{best_solution} = {num}")

if __name__ == "__main__":
    main()