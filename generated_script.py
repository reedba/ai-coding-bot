Problem:
Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. The function should return True if the string is a palindrome, and False otherwise. Ignore spaces and non-alphanumeric characters when checking for palindromes.

Example:
Input: "A man, a plan, a canal: Panama"
Output: True

Explanation:
In the given input, after ignoring spaces and non-alphanumeric characters, the string becomes "amanaplanacanalpanama" which is a palindrome when read backwards.

Solution in Python:

```python
def is_palindrome(s):
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

# Test the function with the example input
input_string = "A man, a plan, a canal: Panama"
print(is_palindrome(input_string))  # Output: True
```

In this solution, we first clean the input string by removing spaces and non-alphanumeric characters using list comprehension and `isalnum()` method. Then, we check if the cleaned string is equal to its reverse (read backward). If they are equal, we return True as the string is a palindrome, otherwise False.