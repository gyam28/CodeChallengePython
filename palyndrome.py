"""
1. PALINDROME CHALLENGE:

Write a function that checks if a given word is a palindrome.
Character case should be ignored.

For example, is_palindrome("Deleveled") should return True
as character case should be ignored, resulting in "deleveled",
which is a palindrome since it reads the same backward and forward.
"""

def is_palindrome(word):
    # YOUR CODE GOES HERE
    if word.lower()[::-1] == word.lower():
        return True
    else:
        return False

print(is_palindrome('Deleveled'))
# This should print True
