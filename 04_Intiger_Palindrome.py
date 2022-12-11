# intiger palindrome
def aIntigerPalindrome(aIntiger):
    if aIntiger == int(str(aIntiger)[::-1]):
        return True
    else:
        return False

# take input from the user
a = print(aIntigerPalindrome(int(input("Enter the intiger: "))))