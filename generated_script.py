Problem:
Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello world"
Output: False

Explanation:
To solve this problem, we can first remove all non-alphanumeric characters from the input string and convert it to lowercase. Then, we can compare the original string with its reverse to determine if it is a palindrome.

Solution in Python:
```python
def is_palindrome(s: str) -> bool:
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello world"))  # Output: False
```

In the solution above, the `is_palindrome` function takes a string `s` as input and first removes all non-alphanumeric characters using list comprehension. Then, it converts all characters to lowercase. Finally, it checks if the modified string is equal to its reverse by using slicing `s[::-1]`. If they are equal, the function returns True, indicating that the input string is a palindrome.