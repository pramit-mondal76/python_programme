start = int(input("Enter the starting number of the range"))
end = int(input("Enter the ending number of the range"))
 
for n in range(start, end+1):
    sum = 0
 
    for i in range(1, n):
        if n%i == 0:
            sum =sum+ i
 
    if n == sum:
        print(n)
