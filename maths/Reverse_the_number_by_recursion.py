##reverse a number using recursion
def reverse(num, rev=0):
    if num == 0:
        print(rev)
    else:
        reverse(num // 10, rev * 10 + num % 10)
num = int(input("Enter a number: "))
reverse(num)