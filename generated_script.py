Problem:
Given a string, implement a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forwards and backwards, ignoring spaces, punctuation, and capitalization.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True (since the above string is a palindrome)

Explanation:
To solve this problem, we can first remove any spaces, punctuation, and convert all characters to lowercase. Then, we can compare the string with its reverse to check if it is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join([c.lower() for c in s if c.isalnum()])
    return s == s[::-1]

# Test the function
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

In the above solution, the `is_palindrome` function takes a string `s` as input and first removes all non-alphanumeric characters and converts all characters to lowercase. Then, it checks if the cleaned string is equal to its reverse using slicing `s[::-1]`. If they are equal, the function returns `True`, indicating that the input string is a palindrome; otherwise, it returns `False`.