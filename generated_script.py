Sure! Here is a new DSA problem that involves strings and arrays:

Problem: Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello"
Output: False

Solution:

```python
def is_palindrome(s):
    s = ''.join(char for char in s if char.isalnum()).lower()
    
    return s == s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama")) # Output: True
print(is_palindrome("racecar")) # Output: True
print(is_palindrome("hello")) # Output: False
```

Explanation:
1. The `is_palindrome` function takes a string `s` as input.
2. We remove all non-alphanumeric characters and convert the string to lowercase using list comprehension.
3. We then compare the string with its reverse to check if it is a palindrome.
4. The function returns `True` if the string is a palindrome, and `False` otherwise.

You can test this solution with different inputs to see if it works correctly. Let me know if you need further clarification or more examples!