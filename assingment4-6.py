a=int(input("enter the first number:"))
b=int(input("Enter the second number:"))

if (a>b):
    smaller=a
else:
    smaller=b   

for i in range (1,smaller+1):
    if((a % i == 0) and (b % i == 0)):
        gcd = i 
print("GCD or HCF is", gcd)        