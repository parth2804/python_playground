## print all prime numbers in a range
a = int(input("Enter start: "))
b = int(input("Enter end: "))
if a>b:
    print("Invalid range")
else:
    for num in range(a, b + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)