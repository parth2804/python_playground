print(list(range(5)))
print(list(range(1, 6)))
print(list(range(2, 11, 2)))
print(list(range(1, 10, 3)))
print(list(range(10, 0, -1)))
print(list(range(20, 10, -2)))
print(list(range(5, -1, -1)))
print(list(range(-5, 6)))
print(list(range(-10, 1, 2)))
print(list(range(10, -1, -2)))
print("Using for loop:")

for i in range(5):
    print(i)

print("Even numbers:")
for i in range(2, 11, 2):
    print(i)

print("Odd numbers:")
for i in range(1, 10, 2):
    print(i)

print("Reverse:")
for i in range(5, 0, -1):
    print(i)