Problem:

Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward.

Example:
Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:
To solve this problem, we can compare the string with its reverse to check if it is a palindrome. If the original string is equal to its reverse, then it is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    # Convert the input string to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

In this solution, we first convert the input string to lowercase and remove any spaces using the `lower()` and `replace()` functions. Then, we check if the string is equal to its reverse using slicing. If they are equal, we return True, indicating that the string is a palindrome.