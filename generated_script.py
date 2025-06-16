Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation: The input string is a palindrome because if we remove all spaces, punctuation, and convert all characters to lowercase, it reads the same forward and backward.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower() # remove spaces, punctuation, and convert to lowercase
    return s == s[::-1]  # check if reversed string is equal to original string 

# Test the function
input_str = "A man, a plan, a canal, Panama"
print(is_palindrome(input_str))  # Output: True
```

The function `is_palindrome` takes a string as input, removes all non-alphanumeric characters and spaces, converts it to lowercase, and then checks if the reversed string is equal to the original string. If they are equal, then the input string is a palindrome and the function returns True, otherwise False.