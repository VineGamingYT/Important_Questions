def is_palindrome(s):
    return s == s[::-1]

s = input("Enter a string: ")

if is_palindrome(s):
    print("Palindrome")
else:
    print("Not a palindrome")
