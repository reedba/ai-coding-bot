Problem:
Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. Ignore spaces, punctuation, and capitalization.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
The input string "A man, a plan, a canal, Panama" when stripped of spaces, punctuation, and converted to lowercase is "amanaplanacanalpanama", which is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

# Test the function
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))                           # Output: True
print(is_palindrome("hello"))                             # Output: False
```

In the above solution, the `is_palindrome` function takes a string `s` as input and removes all non-alphanumeric characters and converts the string to lowercase using list comprehension. Then, it checks if the cleaned string is equal to its reverse (using slicing `[::-1]`) to determine if it is a palindrome.