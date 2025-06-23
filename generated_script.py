Problem:
Given a string, return true if the string is a palindrome, and false if it is not. Ignore case sensitivity and consider only alphanumeric characters.

Example:
Input: s = "A man, a plan, a canal, Panama"
Output: true

Explanation:
The string "A man, a plan, a canal, Panama" is a palindrome because if we remove all non-alphanumeric characters and ignore case sensitivity, it becomes "amanaplanacanalpanama", which reads the same forwards and backwards.

Solution in Python:

```python
def is_palindrome(s):
    clean_str = ''.join(char for char in s if char.isalnum()).lower()
    return clean_str == clean_str[::-1]

# Test the function
s = "A man, a plan, a canal, Panama"
print(is_palindrome(s)) # Output: True
```

In this solution, we first clean up the input string by removing all non-alphanumeric characters and converting it to lowercase. Then, we check if the cleaned string is the same as its reverse, which determines if the input string is a palindrome.