# Find the factorial of a number using recursion - Recursion a function that calls itself until the condition is false
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
