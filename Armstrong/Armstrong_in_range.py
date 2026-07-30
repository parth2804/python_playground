## Armstrong numbers in a range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print("Armstrong numbers in the range:", start, "to", end)
for n in range(start, end + 1):
    p = len(str(n))
    if sum(int(d) ** p for d in str(n)) == n:
        print(n)