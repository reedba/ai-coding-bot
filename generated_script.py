Problem: 

Given a string, implement a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Ignore spaces, capitalization, and punctuation when determining if a string is a palindrome.

Example:

Input: "A man, a plan, a canal, Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:

To solve this problem, we can create a function that takes a string as input and first preprocesses the string by removing spaces, punctuation, and converting all characters to lowercase. 

Next, we can use two pointers technique where we start from the beginning and end of the string and compare characters at each position. If all characters match, we continue moving the pointers towards the middle of the string. If they don't match at any point, we can return False. If we reach the middle of the string and all characters match, we return True.

Solution:

```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama")) # Output: True
print(is_palindrome("racecar")) # Output: True
print(is_palindrome("hello")) # Output: False
```

This function first preprocesses the input string by removing spaces and punctuation, and converting all characters to lowercase. Then, it uses two pointers to compare characters from the start and end of the string, moving towards the middle. If at any point the characters don't match, it returns False. If the pointers meet in the middle of the string, it returns True.