Problem:
Given a string, write a function that returns True if the string is a palindrome, and False otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces and punctuation).

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:
To solve this problem, we can compare the input string with its reverse. If they are the same, then the string is a palindrome. We can ignore spaces and punctuation by using the isalpha() method to check if a character is a letter or not.

Solution in Python:

```python
def is_palindrome(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalpha())
    
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
```

In the solution above, the string is first converted to lowercase and then all non-alphabetic characters are removed using a list comprehension. Finally, the function checks if the modified string is equal to its reverse using slicing. The function returns True if the string is a palindrome and False otherwise.