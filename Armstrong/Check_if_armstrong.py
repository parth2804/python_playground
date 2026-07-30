## Check for Armstrong number
n = input("Enter a number: ")
p = len(n)
s = 0
for d in n:
    s += int(d) ** p
if s == int(n):
    print("Armstrong number")
else:
    print("Not Armstrong number")