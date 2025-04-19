Problem:
Given a string, determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True
Explanation: The string reads the same forward and backward when ignoring spaces, punctuation, and capitalization.

Solution:
```python
def is_palindrome(s):
    s = ''.join([c.lower() for c in s if c.isalnum()]) # Remove spaces, punctuation, and convert to lowercase
    return s == s[::-1]

# Test the function
input_str = "A man, a plan, a canal, Panama"
print(is_palindrome(input_str)) # Output: True
```

Explanation:
1. The function `is_palindrome` takes a string `s` as input.
2. The input string is cleaned by removing spaces, punctuation, and converting to lowercase using list comprehension.
3. The cleaned string is compared with its reversed version using slicing (`[::-1]`) to check if it is a palindrome.
4. The function returns `True` if the string is a palindrome, `False` otherwise.