Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:
To solve this problem, we can iterate through the characters of the string from both ends and compare them. If at any point we find that the characters do not match, we can return False. If we finish iterating through the entire string without finding any mismatches, we can return True.

Solution in Python:

```python
def is_palindrome(s):
    s = s.lower()  # Convert the input string to lowercase for case-insensitive comparison
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# Test the function
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

In the solution above, we define a function `is_palindrome` that takes a string `s` as input. We convert `s` to lowercase using the `lower()` method to make the comparison case-insensitive. We then use two pointers `i` and `j` to iterate through the string from the beginning and end respectively. If at any point the characters at the `i` and `j` indices do not match, we return False. If we successfully iterate through the entire string without returning False, we return True.