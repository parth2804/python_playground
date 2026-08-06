## Check for perfect number
n = int(input("Enter a number: "))
if n <= 1:
    print("Not a perfect number")
else:
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
if s == n:
    print("Perfect number")
else:
    print("Not a perfect number")