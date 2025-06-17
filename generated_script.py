Sure, here is a classic problem involving strings and arrays:

Problem: Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation: To solve this problem, we can check if the input string is equal to its reverse. If they are equal, then the string is a palindrome. Otherwise, it is not a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

This function takes a string `s` as input and checks if it is a palindrome by comparing it to its reverse using string slicing. If the original string is equal to its reverse, then it returns True (indicating that it is a palindrome), otherwise it returns False.