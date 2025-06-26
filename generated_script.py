Problem: Given a string, determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

Explanation: To solve this problem, we can compare each character in the string with its corresponding character from the end of the string. If all characters match, then the string is a palindrome. We can ignore any spaces and make the comparison case-insensitive.

Solution in Python:

```python
def is_palindrome(s):
    s = s.lower()  # Convert string to lowercase
    s = ''.join(e for e in s if e.isalnum())  # Remove non-alphanumeric characters
    
    # Check if the string is a palindrome
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```

In this solution, we first convert the string to lowercase and remove any non-alphanumeric characters. Then, we iterate through the string and compare each character with its corresponding character from the end of the string. If any characters do not match, we return False. Otherwise, we return True at the end.