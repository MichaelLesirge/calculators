import runner
# on calculator there are no folders so runner is in same directory

print("Example number and text calculator")

def add_number_and_str(a, b):
    return a + len(b)

# what inputs do:
#  [("input message", (converter_funtion, "Error message if converter fails" or None to use normal error message) or None to just leave as str)]
runner.run(add_number_and_str, [("Enter first number", (int, "Must enter a number")), ("Enter some text", None)])