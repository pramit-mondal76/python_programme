x=0
y=1
sum=0
print("fibonacci series :-")
for i in range (0,30):
    sum=x+y
    x=y
    y=sum
    if(sum>=10 and sum<=30):
        print(sum)
