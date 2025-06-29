Problem:
Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Solution in Python:

```python
def is_palindrome(s):
    # Removing spaces and converting the string to lowercase
    s = s.replace(" ", "").lower()
    
    # Using two pointers approach to compare characters from start and end of the string
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True

# Test the function with some examples
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```

Explanation:
- The function `is_palindrome` takes a string `s` as input.
- It removes spaces and converts the string to lowercase using the `replace` method.
- It then uses a two pointers approach to compare characters from the start and end of the string.
- If the characters at the start and end don't match, the function returns False.
- If the comparison reaches the middle of the string without any mismatches, the function returns True.
- We test the function with some example strings to verify its correctness.