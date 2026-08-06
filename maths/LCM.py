##LCM of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x=a
y=b 
while b != 0:
    a, b = b, a % b
gcd=a
lcm = abs(x * y) // gcd
print("LCM =", lcm)
