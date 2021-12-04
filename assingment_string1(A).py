str=input("enter any string :")
alphabets=digits=special=space=0

for i in range(len(str)):
    if((str[i] >= 'a'and str[i] <= 'z')or (str[i] >= 'A'and str[i] <= 'Z')):
        alphabets=alphabets+1
    elif(str[i] >= '0'and str[i] <= '9'):
        digits=digits+1
    elif(str[i]==" "):
        space=space+1
    else:
        special=special+1

print("Total  number of alphabets :", alphabets)
print("Total number of Digits :", digits)
print("Total number of space :",space)
print("Total number of Special Characters :", special)

