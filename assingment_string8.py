string=input("Enter any string :")
d1=dict()
for i in string:
    if i in d1:
        d1[i]=d1[i]+1
    else:
        d1[i]=1

print(d1)        
