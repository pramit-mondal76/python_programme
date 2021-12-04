n=int(input("enter any number"))
sum=0
for i in range(1,n):
   if(n%i==0):
    sum=sum+i
if(sum==n):
    print("Given number is a perfect no.")
else:
    print("Given number is not a perfect no.")
