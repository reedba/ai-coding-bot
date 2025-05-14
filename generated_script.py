Problem: 
Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

Example:
Input: "racecar"
Output: True
Explanation: "racecar" reads the same forward and backward, so it is a palindrome.

Input: "hello"
Output: False
Explanation: "hello" does not read the same forward and backward, so it is not a palindrome.

Solution in Python:
```python
def is_palindrome(s):
    s = s.lower()  # Convert the input string to lowercase
    s = ''.join(char for char in s if char.isalnum())  # Remove non-alphanumeric characters
    
    left, right = 0, len(s) - 1  # Pointers for the left and right indices of the string
    
    while left < right:
        if s[left] != s[right]:  # If characters at left and right indices are not equal, return False
            return False
        left += 1
        right -= 1
    
    return True  # If the while loop completes without returning False, the string is a palindrome

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
```