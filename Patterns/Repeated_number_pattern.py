##Print repeated-number pattern.
## 1
## 22
## 333
## 4444
## 55555
n=int(input("Enter the number of rows: "))  
for i in range(1, n + 1):
    print(str(i) * i)   
##for i in range(1, n + 1):
##    for j in range(i):
##        print(i, end="")
##    print()