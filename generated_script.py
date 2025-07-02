Problem: Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward.

Explanation:
To determine if a string is a palindrome, we can compare the original string with its reverse. If the two strings are equal, then the original string is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    # Remove all non-alphanumeric characters and convert the input string to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Compare the original string with its reverse
    return s == s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama")) # True
print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False
```

In this solution, we first remove all non-alphanumeric characters and convert the input string to lowercase. Next, we compare the original string with its reverse using slicing. If the two strings are equal, we return True, indicating that the string is a palindrome.