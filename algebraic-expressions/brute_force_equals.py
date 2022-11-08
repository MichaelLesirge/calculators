from algebraic_expression import Expression

class ExpressionInputError(ValueError):
    pass

min_possible = 0
max_possible = 360

leave_keywords = {"ex", "exit", "leave", "quit", "get me out of here"}

print("Brute force problem solver")

print('Example input: "3x + 1 = 7"')

def set_eqaul(v: Expression, i: int|float) -> Expression:
    return (v.set_eqaul(i) if v.unique_bases_count > 0 else v)

while True:
    print()
    user_input = input("Enter question: ")

    if user_input in leave_keywords:
        print("Bye Bye")
        exit()

    try:
        split_input = user_input.split("=")

        if len(split_input) < 2:
            raise ExpressionInputError("Problem must have left and right side seprated by equal sign")

        vals = [Expression(v.strip()) for v in split_input]

        if any(((v.unique_bases_count > 1) for v in vals)):
            raise ExpressionInputError("All expression must be monomials (only have 1 varible)")
            

        for v in vals:
            try:
                var = v._get_base
                break
            except Exception:
                continue
        else:
            raise ExpressionInputError("Must have at lease 1 variable")
            

        if any(((v.unique_bases_count == 1 and v._get_base != var) for v in vals)):
            raise ExpressionInputError("Can only have one varible accros all expression")

        compare_expression, *expressions = vals

        for i in range(min_possible, max_possible+1):
            compare = set_eqaul(compare_expression, i)

            if all((set_eqaul(v, i) == compare for v in expressions)):
                print(f"{var} = {i}")
                break
        else:
            print(f"No valid value for {var}")
    except ExpressionInputError as ex:
        print(ex)