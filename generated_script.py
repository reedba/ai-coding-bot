Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. 

Input: A string
Output: True if the string is a palindrome, False otherwise

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Solution in Python:

```python
def is_palindrome(s):
    # Convert the string to lowercase and remove all non-alphanumeric characters
    s = ''.join(e for e in s.lower() if e.isalnum())
    
    # Two pointers approach to check if the string is a palindrome
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Test the function
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
```

Explanation:
- The function `is_palindrome` takes a string `s` as input and first converts it to lowercase and removes all non-alphanumeric characters using a list comprehension.
- We then use a two pointers approach to check if the string is a palindrome. We initialize two pointers `left` (starting from the beginning) and `right` (starting from the end) and compare the characters at these indexes. If they are not equal, we return False. If we reach the middle of the string without any mismatches, the string is a palindrome and we return True.

The given solution efficiently checks if a given string is a palindrome in Python using a two-pointers approach.