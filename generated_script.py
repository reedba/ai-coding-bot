Problem: Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Ignore non-alphanumeric characters and case sensitivity.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation: The input string, "A man, a plan, a canal, Panama", is a palindrome when non-alphanumeric characters are ignored and case is ignored. When the non-alphanumeric characters and case are removed, the string becomes "amanaplanacanalpanama", which reads the same backward as forward.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Test the function with the given example
input_string = "A man, a plan, a canal, Panama"
print(is_palindrome(input_string))  # Output: True
```

In the solution code, we first clean up the input string by removing non-alphanumeric characters and converting all characters to lowercase. Then, we check if the cleaned up string is equal to its reverse. If they are equal, then the input string is a palindrome and the function returns True.