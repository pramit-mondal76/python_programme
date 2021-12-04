num=int(input("Enter a number:"))
sum=0
temp=num1=num
cnt=0
while num1>0:
    cnt=cnt+1
    num1=num1//10
while temp>0:
    digit=temp%10
    sum =sum+digit ** cnt
    temp=temp//10

if num==sum:
    print( "no is amstrong no.")

else:
    print( "no is not amstrong no.")
