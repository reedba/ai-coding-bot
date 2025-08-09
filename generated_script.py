Problem: 

Given a string, determine if it is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Ignore whitespaces, punctuation, and capitalization.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
The input string, "A man, a plan, a canal, Panama", is a palindrome when we remove whitespaces, punctuation, and capitalization. The string reads the same forwards and backwards.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

# Test the function
input_str = "A man, a plan, a canal, Panama"
print(is_palindrome(input_str))  # Output: True
```

In this solution, the `is_palindrome` function takes a string as input. We remove whitespaces and punctuation using `filter(str.isalnum, s)` and convert the string to lowercase using `lower()`. Then we compare the string to its reverse (`s == s[::-1]`) to determine if it is a palindrome.