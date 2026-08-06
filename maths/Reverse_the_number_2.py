## reverse a number
num = input("Enter a number: ")
rev = ""
for digit in num:
    rev = digit + rev
print("Reverse of the number is", rev)