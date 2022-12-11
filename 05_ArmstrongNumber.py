# armstrong number is a number that is equal to the sum of cubes of its digits
def armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        return True
    else:
        return False
    
# take input from the user
a = print(armstrong(int(input("Enter the number: "))))