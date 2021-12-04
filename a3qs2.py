n=int(input("Enter number:"))
temp=n
r =0
while(n>0):
    x=n%10
    r =r *10+x
    n=n//10
if(temp==r):
    print("The number is a palindrome.")
else:
    print("The number isn't a palindrome.")
