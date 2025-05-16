Problem:
Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequences of characters which reads the same backward as forward. Ignore capitalization, spaces, and punctuation.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello"
Output: False

Solution (in Python):

```python
def is_palindrome(s):
    # Remove spaces, punctuation, and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if string is palindrome
    return s == s[::-1]

# Test the function
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
```

Explanation:

1. The `is_palindrome` function takes a string `s` as input.
2. We remove spaces and punctuation from the input string by using a list comprehension that iterates over each character in the string and only keeps alphanumeric characters.
3. We convert all characters to lowercase to ignore case sensitivity.
4. We then check if the cleaned version of the string is equal to its reverse (using slicing with `[::-1]`). If they are equal, the input string is a palindrome and the function returns True, otherwise, it returns False.
5. We test the function with a few examples to demonstrate its functionality.