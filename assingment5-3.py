string=input("enter any string:")
index=int(input("Enter the removing index : "))
new_string=''
for i in range(0,len(string)):
    if(i!=index):
        new_string=new_string+string[i]
print("The string after removing the index is:")
print(new_string)        
