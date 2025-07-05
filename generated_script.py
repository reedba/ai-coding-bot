Problem: Given a string, write a function to determine if it is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:
To solve this problem, we first need to remove all non-alphanumeric characters and convert the string to lowercase. Then, we can compare the string with its reverse and check if they are equal. If they are equal, then the string is a palindrome.

Solution in Python:
```python
def is_palindrome(s):
    s = ''.join(e.lower() for e in s if e.isalnum())
    return s == s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama")) # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

In this solution, we first remove all non-alphanumeric characters and convert the string to lowercase using a list comprehension. Then, we compare the modified string with its reverse using slicing and return True if they are equal, indicating that the string is a palindrome.