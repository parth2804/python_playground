## convert a binary number to decimal
binary = input("Enter binary number: ")
decimal = 0
power = len(binary) - 1
for digit in binary:
    decimal += int(digit) * (2 ** power)
    power -= 1
print(decimal)