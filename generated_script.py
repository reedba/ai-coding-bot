Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.

Explanation: To check if a string is a palindrome, we can compare the string with its reverse. If the reversed string is the same as the original string, then the string is a palindrome.

Solution in Python:
```python
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    if s == s[::-1]:
        return True
    else:
        return False

# Test the function
print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```

This function first removes spaces and converts the string to lowercase. Then, it compares the string with its reverse using slicing. If they are the same, it returns True, indicating that the string is a palindrome.