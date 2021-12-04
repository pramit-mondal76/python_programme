str1=input("Enter the first string :")
str2=input("Enter the second string :")
if(len(str1)==len(str2)):
    if(sorted(str1)==sorted(str2)):
        print("The two strings are anagram.")
        
    else:
        print("The two strings are not anagram.")

else:
   print("The two strings are not anagram.")       
