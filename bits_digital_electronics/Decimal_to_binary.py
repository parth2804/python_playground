## convert a decimal number to binary
decimal = int(input("Enter decimal number: "))
binary = ""
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2
print(binary)