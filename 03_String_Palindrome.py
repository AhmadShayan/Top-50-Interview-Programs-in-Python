# string palindrome
def aStringPalindrome(aString):
    if aString == aString[::-1]:
        return True
    else:
        return False
    
# take input from the user
a = print(aStringPalindrome(input("Enter the string: ")))