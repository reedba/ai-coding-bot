Problem: 

Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. Ignore capitalization, spaces, and punctuation in determining if the string is a palindrome.

Example: 
Input: "A man, a plan, a canal: Panama"
Output: True 

Explanation:
In the given example, the string "A man, a plan, a canal: Panama" is a palindrome when all non-alphanumeric characters and case are ignored. The reversed string is "amanaplanacanalpanama", which is the same as the original string.

Solution in Python:

```python
def is_palindrome(s):
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    return normalized_str == normalized_str[::-1]

# Test the function with the example
input_str = "A man, a plan, a canal: Panama"
print(is_palindrome(input_str))  # Output: True
```

In the solution provided, the `is_palindrome` function takes a string as input and returns a boolean value indicating whether the string is a palindrome. 
- First, it normalizes the input string by converting it to lowercase and removing any non-alphanumeric characters.
- Then, it compares the normalized string with its reversed version to determine if it is a palindrome.
- Lastly, it returns `True` if the string is a palindrome and `False` otherwise.

You can test the function with different input strings to see if it correctly identifies palindromes.