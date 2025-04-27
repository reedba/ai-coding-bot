Problem: Given a string, implement a function to check if it is a palindrome. A palindrome is a word or phrase that is the same forwards and backwards, ignoring spaces, punctuation, and capitalization.

Explanation: To solve this problem, we can first remove all non-alphanumeric characters and convert the string to lowercase. Then, we can compare the original string with its reversed version to determine if it is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join([c.lower() for c in s if c.isalnum()]) # Remove non-alphanumeric characters and convert to lowercase
    return s == s[::-1] # Compare original string with reversed string

# Test the function
input_str = "A man, a plan, a canal, Panama"
print(is_palindrome(input_str)) # Output: True

input_str = "racecar"
print(is_palindrome(input_str)) # Output: True

input_str = "hello world"
print(is_palindrome(input_str)) # Output: False
```

In this solution, we use list comprehension to filter out non-alphanumeric characters and convert all characters to lowercase. We then compare the original string with its reverse using slicing. If the two strings are the same, the function returns True, indicating that the input string is a palindrome.