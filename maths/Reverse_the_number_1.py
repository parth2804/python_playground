## reverse a number
num = int(input("Enter a whole number number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev)