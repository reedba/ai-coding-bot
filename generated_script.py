Problem:
Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward. Ignore case sensitivity and remove all non-alphanumeric characters before checking if the string is a palindrome.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
After removing all non-alphanumeric characters and converting the string to lowercase, the input string becomes "amanaplanacanalpanama" which is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

# Test the function
print(is_palindrome("A man, a plan, a canal, Panama")) # Output: True
print(is_palindrome("race a car")) # Output: False
```

In the solution, we first remove all non-alphanumeric characters from the input string using the filter function and convert it to lowercase. Then, we check if the modified string is equal to its reverse by comparing it with `s[::-1]`, which is the string reversed. If the two strings are equal, we return True indicating that the input string is a palindrome. Otherwise, we return False.