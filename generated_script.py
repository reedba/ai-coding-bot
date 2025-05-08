Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Explanation:
To solve this problem, we can first remove all non-alphanumeric characters from the input string and convert it to lowercase. Then, we can compare the string with its reverse to check if it is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())  # Remove non-alphanumeric characters and convert to lowercase
    return s == s[::-1]  # Check if the string is equal to its reverse

# Test the function
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False
```

In the above solution, we use list comprehension to create a new string `s` with only alphanumeric characters in lowercase. Then, we check if this new string is equal to its reverse using slicing. The function returns `True` if the input string is a palindrome, and `False` otherwise.