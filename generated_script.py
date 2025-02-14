Problem: Write a Python function to check if a string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.

Explanation: In this problem, we need to check if a given string is a palindrome or not. To do this, we can compare the original string with its reverse. If the two strings are the same, then the given string is a palindrome.

Solution:

```python
def is_palindrome(s):
    s = s.lower()  # Convert string to lowercase for case-insensitive comparison
    s = ''.join(e for e in s if e.isalnum())  # Remove non-alphanumeric characters

    # Compare original string with its reverse
    return s == s[::-1]

# Test the function
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```

In the solution, we first convert the string to lowercase using `lower()` method to make the comparison case-insensitive. Then, we remove non-alphanumeric characters using a generator expression and `join()` method. Finally, we compare the original string with its reverse using slicing.

The function `is_palindrome` returns `True` if the string is a palindrome and `False` otherwise. We test the function with a few examples to verify its correctness.