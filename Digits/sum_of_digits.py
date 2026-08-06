## sum of digits of a number
num = input("Enter a natural number: ")
sum = 0
for digit in num:
    sum += int(digit)
print("Sum of digits =", sum)