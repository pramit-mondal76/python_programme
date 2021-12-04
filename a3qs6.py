age = int(input('Please enter a persons age.'))

if age == 1:
    print ("is born")
elif age > 1 and age <= 10:
    print ("is child")
elif age >= 12 and age < 18:
    print ("is young")
elif  age >= 18 and age<50 :
    print ("is adult")
elif  age >= 50 and age<80 :
    print ("is old")
elif  age >=80 :
    print ("is very old")
    
    
else:
    print ("wrong age")
