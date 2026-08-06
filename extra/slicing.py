a = """this is python class"""

print("Original String:", a)

print(a[:])
print(a[::-1])
print(a[::2])
print(a[::-2])

print(a[:7])
print(a[8:14])
print(a[15:])
print(a[8:20])
print(a[8:20:2])

print(a[13:7:-1])
print(a[-1::-1])
print(a[-5:])
print(a[-5::-1])

print(a[0])
print(a[5])
print(a[-1])
print(a[-6])

print(a[::3])
print(a[1::2])
print(a[2::3])

print("Length =", len(a))