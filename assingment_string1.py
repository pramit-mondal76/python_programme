str=input("enter any string :")
alphabets=digits=special=space=0

for i in range(len(str)):
    if(str[i].isalpha()):
        alphabets=alphabets+1
    elif(str[i].isdigit()):
        digits=digits+1
    elif(str[i].isspace()):
        space=space+1
    else:
        special=special+1

print("Total  number of alphabets :", alphabets)
print("Total number of Digits :", digits)
print("Total number of space :",space)
print("Total number of Special Characters :", special)

