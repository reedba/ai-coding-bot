Problem:
Given a string, write a Python function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Ignore spaces, punctuation, and capitalization.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:
To solve this problem, we can first remove all non-alphanumeric characters and convert the string to lowercase. Then, we can compare the characters from the start of the string with the characters from the end of the string to determine if it is a palindrome.

Solution:
```python
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```

This function will remove all non-alphanumeric characters, convert the string to lowercase, and then check if it is a palindrome by comparing characters from the start and end of the string.