Sure! Here's a problem for you to work on:

Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forwards and backwards. The function should return True if the input string is a palindrome and False otherwise.

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Solution in Python:

```python
def is_palindrome(s):
    s = s.lower()  # convert the input string to lowercase
    left, right = 0, len(s) - 1  # initialize two pointers at the beginning and end of the string
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
```

You can run this code to test the function and see if it correctly identifies palindromes in strings. Let me know if you need any further explanation or help with this problem!