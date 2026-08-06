t = input("Enter type (dec/bin/oct/hex): ")
n = input("Enter number: ")

if t == "dec":
    a = int(n)
elif t == "bin":
    a = int(n, 2)
elif t == "oct":
    a = int(n, 8)
elif t == "hex":
    a = int(n, 16)
else:
    print("Invalid type")

c = input("Convert to (bin/oct/hex/all): ")

if c == "bin":
    print(bin(a))
elif c == "oct":
    print(oct(a))
elif c == "hex":
    print(hex(a))
elif c == "all":
    print("Decimal:", a)
    print("Binary:", bin(a))
    print("Octal:", oct(a))
    print("Hex:", hex(a))
else:
    print("Invalid choice")