Problem: Given a string, write a function to check if it is a palindrome (a word, phrase, number, or other sequence of characters which reads the same backward as forward).

Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation: 
To solve this problem, we can check if the string is equal to its reverse. We can achieve this by using string slicing in Python.

Solution:

```python
def is_palindrome(s):
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False
print(is_palindrome("level")) # True
```

In this solution, the function `is_palindrome` takes a string `s` as input and returns True if the string is equal to its reverse (i.e., a palindrome), and False otherwise. The `[::-1]` syntax is used to reverse the string `s`.

The test cases show the function in action, with "racecar" and "level" returning True (as they are palindromes) and "hello" returning False.