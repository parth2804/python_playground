## multiplication table of a number
num = int(input("Enter a number: "))
print("Multiplication table of", num, "is:")
for a in range(1, 11):
    print(num, "x", a, "=", num * a)