Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.

Explanation: To check if a string is a palindrome, we can compare the string with its reverse. If the reversed string is the same as the original string, then the string is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar")) # Output: True
print(is_palindrome("hello")) # Output: False
print(is_palindrome("1221")) # Output: True
print(is_palindrome("apple")) # Output: False
```

In the above solution, the `is_palindrome` function takes a string `s` as input and returns `True` if it is a palindrome, and `False` otherwise. The function uses slicing (`[::-1]`) to reverse the string and compare it with the original string.