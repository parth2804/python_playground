## factorial of a number using recursion
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a number: "))
print(n, "! =", factorial(n))