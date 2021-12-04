n = int(input("Enter an integer: "))
for i in range(2, n + 1):
    if n % i == 0:
        print("Smallest divisor is:", i)
        break
