Problem: Given a string, implement a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

For example:
Input: "A man, a plan, a canal, Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello"
Output: False

Solution:
```python
def is_palindrome(s):
    # Remove spaces and punctuation, convert to lowercase
    s = ''.join(e.lower() for e in s if e.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))   # Output: True
print(is_palindrome("racecar"))                           # Output: True
print(is_palindrome("hello"))                             # Output: False
```

Explanation:
1. The `is_palindrome` function takes a string `s` as input.
2. Using a list comprehension, we remove spaces and punctuation using the `isalnum` function and convert all characters to lowercase.
3. We check if the modified string is equal to its reverse using the slicing notation `[::-1]`.
4. The function returns `True` if the string is a palindrome and `False` otherwise.
5. Test cases are provided to verify the function's correctness.