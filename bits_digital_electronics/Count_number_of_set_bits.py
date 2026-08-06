## count number of set bits
n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += n % 2
    n //= 2

print(count)