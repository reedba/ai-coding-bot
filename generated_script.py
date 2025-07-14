Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Example:

Input: "A man, a plan, a canal, Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello world"
Output: False

Explanation: 
To solve this problem, we can first clean up the input string by removing any non-alphanumeric characters and converting all characters to lowercase. Then, we can compare the cleaned-up string with its reverse to determine if it is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello world"))  # Output: False
```

This function takes a string `s` as input, cleans it up by removing non-alphanumeric characters and converting all characters to lowercase. It then checks if the cleaned-up string is equal to its reverse using slicing (`[::-1]`) and returns `True` if it is a palindrome, and `False` otherwise.