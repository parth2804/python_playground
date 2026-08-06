# year = int(input("Enter year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("This is a leap year")
# else:
#     print("This is not a leap year")










year = int(input("Enter year: "))

if year % 400 == 0:
    print("This is a leap year")
elif year % 100 == 0:
    print("This is not a leap year")
elif year % 4 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")