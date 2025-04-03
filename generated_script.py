Problem:
Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:
To check if a string is a palindrome, we can compare the characters at the beginning and end of the string. If they are the same, we move towards the center of the string until we have checked all characters. If at any point the characters do not match, the string is not a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("madam"))    # True
```

This function takes a string `s` as input and uses two pointers `left` and `right` to compare the characters at the beginning and end of the string. If the characters do not match, the function returns False. If all characters match, the function returns True, indicating that the string is a palindrome.