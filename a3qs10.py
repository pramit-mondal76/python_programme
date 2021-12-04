n=int(input("Enter the number: "))
k=1
for i in range(0,n):
    k=i
    for m in range(n-1,i,-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        k=k+1
        print(k,end=" ")
    print()
