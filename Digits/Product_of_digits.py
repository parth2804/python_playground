## product of digits of a number
num = input("Enter a natural number: ")
product = 1
for digit in num:
    product *= int(digit)
print("Product of digits =", product)