Problem: Given a string, write a function to determine if it is a palindrome. A palindrome is a string that reads the same forwards as backwards, ignoring spaces, capitalization and punctuation.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
In the given string "A man, a plan, a canal, Panama", if we remove spaces, punctuation and convert all letters to lowercase, the string becomes "amanaplanacanalpanama" which is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Test the function with the example input
input_str = "A man, a plan, a canal, Panama"
print(is_palindrome(input_str))  # Output: True
```

In this solution, the `is_palindrome` function takes a string `s` as input. It first filters out non-alphanumeric characters using a list comprehension and converts all letters to lowercase. Then, it checks if the filtered string is equal to its reverse (achieved by slicing with `[::-1]`). If they are equal, the function returns True, indicating that the input string is a palindrome.