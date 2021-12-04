n= input("Enter the first string: ")
n2= input("Enter the second string: ")
n3= input("Enter the third string: ")
v=""
c=""
l=""
for i in range(len(n)):
    if(n[i]=='a'or n[i]=='e'or n[i]=='i'or n[i]=='o'or n[i]=='u'or n[i]=='A'or n[i]=='E'or n[i]=='I'or n[i]=='O'or n[i]=='U'):
        v=v+'$'
    else:
        v=v+n[i]
for i in range(len(n2)):
    if(n2[i]!='a'and n2[i]!='e'and n2[i]!='i'and n2[i]!='o'and n2[i]!='u'and n2[i]!='A'and n2[i]!='E'and n2[i]!='I'and n2[i]!='O'and n2[i]!='U'):
        c=c+'*'
    else:
        c=c+n2[i]
for i in range(len(n3)):
    if(n3[i].isupper()):
        l=l+n3[i].lower()
    else:
        l=l+n3[i]
print(v)
print(c)
print(l)
