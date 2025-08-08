Problem: 
Given a string, write a Python function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, capitalization, and punctuation).

Explanation:
To solve this problem, we can remove all non-alphanumeric characters from the input string and convert it to lowercase. Then we can compare the original string with its reverse to determine if it is a palindrome.

Solution:

```python
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = "".join(char.lower() for char in s if char.isalnum())
    
    # Compare original string with its reverse
    return s == s[::-1]

# Test the function
test_string1 = "A man, a plan, a canal, Panama!"
test_string2 = "racecar"
test_string3 = "hello"

print(is_palindrome(test_string1))  # True
print(is_palindrome(test_string2))  # True
print(is_palindrome(test_string3))  # False
```

This function first removes all non-alphanumeric characters from the input string using list comprehension and the `isalnum()` method. Then it converts the remaining characters to lowercase. Finally, it checks if the modified string is equal to its reverse using slicing.