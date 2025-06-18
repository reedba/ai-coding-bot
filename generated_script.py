Problem:
Given a string, write a function in Python to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
In the given example, the input string is "A man, a plan, a canal, Panama". If we remove spaces, punctuation, and consider only lowercase characters, the string becomes "amanaplanacanalpanama", which is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    # Removing spaces and punctuation and converting to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Checking if the string is a palindrome
    return s == s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello world"))  # Output: False
```

In the solution provided, we first remove spaces and punctuation from the input string and convert it to lowercase. We then check if the modified string is equal to its reverse (using slicing with `[::1]`), which determines if the string is a palindrome or not.