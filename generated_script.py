Problem: 

Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Ignore capitalization, spaces, and punctuation.

Example:

Input: "A man, a plan, a canal, Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello world"
Output: False

Explanation:

To solve this problem, we can create a function that takes a string as input and then removes all non-alphanumeric characters from the string using regex. Then we can compare the original string and its reverse to see if they are the same, indicating that the string is a palindrome.

Solution:

```python
import re

def is_palindrome(s):
    s = re.sub('[^A-Za-z0-9]', '', s).lower()
    return s == s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama")) # True
print(is_palindrome("racecar")) # True
print(is_palindrome("hello world")) # False
```

In this solution, we first remove all non-alphanumeric characters from the string using the `re.sub` function with a regex pattern. Next, we convert the string to lowercase and compare it with its reverse using `s == s[::-1]` to check if it is a palindrome. Finally, we test the function with some sample inputs to verify its correctness.