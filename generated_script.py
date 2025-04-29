Sure! Here's a new DSA problem involving strings and arrays:

Problem:
Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
In the given input, the string reads the same forward and backward when ignoring spaces, punctuation, and capitalization. Therefore, the output is True.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

# Test the function
input_str = "A man, a plan, a canal, Panama"
print(is_palindrome(input_str)) # Output: True
```