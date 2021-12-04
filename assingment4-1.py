str=input("enter any string :")
letters= digits = 0

for c in str:
    if ((c>='a' and c<='z') or (c>='A' and c<='Z')):
        letters =letters+1
    if (c>='0' and c<='9'):
       digits=digits+1

print("Total number of letters: ", letters)
print("Total number of digits: ", digits)