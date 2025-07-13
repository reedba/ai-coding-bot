Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. 

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:

We can solve this problem by comparing the string with its reverse. If the reverse of the string is equal to the original string, then the string is a palindrome. We can use Python built-in functions to reverse the string and compare it with the original string.

Solution in Python:

```python
def is_palindrome(s):
    # Remove spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    # Compare the original string with its reverse
    return s == s[::-1]

# Test the function with examples
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True
```

In the solution above, we first remove spaces and convert the string to lowercase using the `replace()` and `lower()` functions. Then, we compare the original string with its reverse using slicing notation `s[::-1]`. If they are equal, we return `True` indicating that the string is a palindrome, otherwise `False`.