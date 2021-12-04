s=input("Enter any string:")
s.lower()
count=1
for i in s:
    if s.count(i)== ord(i)-96 :
        count =1
    else:
        count=0
        break
if count++1:
    print("superascii.")     
else:
    print("Not superascii.")       