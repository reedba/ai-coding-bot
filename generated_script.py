Problem: 
Given a string, check if it is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. The input string will only contain lowercase letters and no spaces.

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:
To solve this problem, we can check if the string is equal to its reverse. If it is, then it is a palindrome. We can reverse the string using Python's slicing syntax. So, we can compare the original string with its reverse to determine if it is a palindrome or not.

Solution in Python:

```python
def is_palindrome(s):
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
```

In this solution, the `is_palindrome` function takes a string `s` as input and returns a boolean value indicating whether the string is a palindrome or not. It does this by comparing the original string with its reverse using slicing syntax `s[::-1]`. If they are equal, then the string is a palindrome and the function returns `True`, otherwise it returns `False`.