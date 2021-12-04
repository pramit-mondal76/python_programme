str=input("enter any string :")
vowels=consonants=others=0
for i in range(0,len(str)):   
    if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u' or str[i]=='A' or str[i]=='E' or str[i]=='I' or str[i]=='O' or str[i]=='U'):
      vowels=vowels+1
    elif((str[i] >= 'a'and str[i] <= 'z')or (str[i] >= 'A'and str[i] <= 'Z')):
      consonants = consonants + 1
    else :
      others=others+1

print("The no of vowels :",vowels)
print("The no of consonants :",consonants)
print("others :",others)

        
