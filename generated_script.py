Problem: 

Given a string, write a function to determine if it is a palindrome. A palindrome is a word or phrase that reads the same backward as forward.

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:

A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. In this problem, we are given a string and we need to check if it is a palindrome.

Solution:

```python
def is_palindrome(s):
    # Removing all non-alphanumeric characters and converting to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar")) # Output: True
print(is_palindrome("hello"))   # Output: False
print(is_palindrome("A man, a plan, a canal, Panama")) # Output: True
```

In the solution, we first remove all non-alphanumeric characters and convert the string to lowercase. Then, we check if the string is equal to its reverse using slicing `s[::-1]`. If they are equal, we return True indicating that the string is a palindrome, otherwise we return False.