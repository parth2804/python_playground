## Strong number
n = input("Enter a number: ")
s = 0
for d in n:
    fact = 1
    for i in range(1, int(d) + 1):
        fact *= i
    s += fact

if s == int(n):
    print("Strong number")
else:
    print("Not a Strong number")