Problem:
Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequences of characters that read the same forward and backward (ignoring spaces, capitalization, and punctuation).

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello world"
Output: False

Explanation:
To solve this problem, we can first remove all non-alphanumeric characters from the input string and convert it to lowercase. Then we can compare the string with its reverse to check if it is a palindrome.

Solution:
```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello world"))  # Output: False
``` 

This function first removes all non-alphanumeric characters from the input string and converts it to lowercase using list comprehension. Then it compares the modified string with its reverse using slicing to determine if it is a palindrome.