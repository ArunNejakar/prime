num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
    num = int(input("Enter a number: "))

# Even or Odd
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Prime check
if num < 2:
    print(f"{num} is not prime.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime.")
            break
    else:
        print(f"{num} is prime.")

