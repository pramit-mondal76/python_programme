str=input("enter any string :")
digits = 0

for c in str:
    if (c>='0' and c<='9'):
           digits=digits+1

print("Total number of digits: ", digits)