Problem:

Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Ignore spaces, punctuation, and capitalization when determining if a string is a palindrome.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
The input string "A man, a plan, a canal, Panama" can be read the same way forwards and backwards when ignoring spaces, punctuation, and capitalization. Therefore, the output is True.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(char for char in s if char.isalnum()).lower()
    return s == s[::-1]

# Test the function with example input
input_string = "A man, a plan, a canal, Panama"
print(is_palindrome(input_string))  # Output: True
```

In the solution, the `is_palindrome` function takes a string as input and first removes all non-alphanumeric characters (using list comprehension and the `isalnum()` method) and converts all characters to lowercase. Then, it checks if the cleaned string is equal to its reverse (achieved by slicing with `[::-1]`), returning `True` if it is a palindrome.