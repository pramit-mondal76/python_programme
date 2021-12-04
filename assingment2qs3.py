n=int(input("Enter any number"))
c=0
if n>1:
      for i in range(1,n+1):
        if(n%i==0):
          c=c+1
      if(c==2):
            print("The no is prime.")
      else:
            print("The no is not prime")
else:
  print("Wrong number")
