n =int(input("Enter any number"))
if n%3==0:
     if n%7==0:
       print(n,"the no is divisible by both 7 and 3")
     else:
       print(n,"the no is divisible by  3")
if n%7==0:
     if n%3==0:
       print(n,"the no is divisible by both 7 and 3")
     else:
       print(n,"the no is divisible by 7")
else:
     print(n,"the no is not divisible by both 3 and 7")
    
