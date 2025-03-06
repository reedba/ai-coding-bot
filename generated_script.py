Problem: Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello world"
Output: False

Explanation:
To solve this problem, we can first remove all non-alphanumeric characters and convert the input string to lowercase. Then, we can compare the string with its reverse to determine if it is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello world"))  # False
```

This function first removes all non-alphanumeric characters from the input string `s` by using a list comprehension with the built-in `isalnum()` method. It then converts the string to lowercase using the `lower()` method. Finally, it compares the cleaned string `s` with its reverse, obtained using slicing `s[::-1]`, to determine if it is a palindrome.