Problem: 
Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:
To solve this problem, we can compare the original string with the reverse of the string. If they are equal, then the string is a palindrome. We can create the reverse of the string by using slicing in Python.

Solution:
```python
def is_palindrome(s):
    return s == s[::-1]

#Test cases
print(is_palindrome("racecar")) #True
print(is_palindrome("hello")) #False
```

In this solution, we are using string slicing in Python to reverse the string `s`. Then, we are comparing the original string `s` with the reversed string `s[::-1]`. If they are equal, then the function returns True indicating that the string is a palindrome, otherwise it returns False.