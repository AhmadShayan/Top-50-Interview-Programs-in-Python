# return factorial of a number
def getFactorial(n):
    if n == 0:
        return 1
    else:
        return n * getFactorial(n-1)
    
# take input from user
a = print(getFactorial(int(input("Enter the number: "))))
          