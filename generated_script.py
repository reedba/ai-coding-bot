Problem: 

Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forwards and backwards. 

Example:
Input: "racecar" 
Output: True 

Input: "hello" 
Output: False

Explanation: 
To solve this problem, we can compare the original string with its reverse. If they are the same, then the string is a palindrome. We can ignore any spaces, special characters, or letter case by converting the string to lowercase and removing any non-alphanumeric characters. 

Solution in Python:

```python
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(filter(str.isalnum, s)).lower()
    
    # Compare the original string with its reverse
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

This function first removes any non-alphanumeric characters using the `filter()` function with `str.isalnum`, and then converts the string to lowercase using `lower()`. It then compares the original string `s` with its reverse using slicing `s[::-1]` to check if it is a palindrome.