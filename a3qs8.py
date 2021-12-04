n=int(input("Enter the number: "))

for i in range(0,n):
    for j in range(i+1,0,-1):
        print("*",end=" ")
    print()
