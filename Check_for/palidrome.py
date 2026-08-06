## check if a number is palindrome or not
num = input("Enter a number: ")
rev = ""
for digit in num:
    rev = digit + rev
if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")