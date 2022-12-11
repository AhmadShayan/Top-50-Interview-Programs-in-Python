def checkPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
    
# take input from the user
a = checkPrime(int(input("Enter the number: ")))
if a is True:
    print("The number is prime")
else:
    print("The number is not prime")