string=input("Enter any string:")
new_string=''
for i in range(len(string)):
    if(i%2==0):
      new_string=new_string+string[i] 
print("Now the string is:",new_string)      