Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Solution:
```python
def is_palindrome(s):
    # remove any spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    
    # check if the string is equal to its reverse
    if s == s[::-1]:
        return True
    else:
        return False

# Test the function with some examples
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

Explanation:
1. The function takes a string `s` as input.
2. The `replace()` method is used to remove any spaces in the string and the `lower()` method is used to convert the string to lowercase.
3. We then compare the original string `s` with its reverse `s[::-1]`. If they are equal, the function returns True (indicating a palindrome), otherwise it returns False.