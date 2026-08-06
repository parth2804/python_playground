##largest prime factor of a given natural number
n = int(input("Enter a natural number: "))
largest = 1
for i in range(2, n + 1):
    while n % i == 0:
        largest = i
        n //= i
print("Largest prime factor:", largest)