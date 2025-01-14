#!/usr/bin/python3
# The shebang line specifies the Python 3 interpreter to execute this script.

import sys
# Importing the sys module to handle command-line arguments.

def factorial(n):
    # This function calculates the factorial of a given number 'n' recursively.
    if n == 0:
        # Base case: The factorial of 0 is defined as 1.
        return 1
    else:
        # Recursive case: Multiply the current number 'n' by the factorial of 'n-1'.
        return n * factorial(n - 1)

# Retrieve the command-line argument, convert it to an integer, and pass it to the factorial function.
# The result is stored in the variable 'f'.
f = factorial(int(sys.argv[1]))

# Print the result (factorial of the input number) to the console.
print(f)
