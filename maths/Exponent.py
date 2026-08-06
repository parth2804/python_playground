## calculate x^n using a loop and not ** operator
base = int(input("Enter base (x): "))
exp = int(input("Enter exponent (n): "))
result = 1
for i in range(exp):
    result *= base
print(result)