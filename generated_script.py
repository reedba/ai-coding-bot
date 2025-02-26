Problem: 

Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. For example, "racecar" and "madam" are palindromes.

Explanation:

To solve this problem, we can compare the original string with its reverse. If they are the same, then the string is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase
    s = ''.join(c for c in s if c.isalnum())  # Remove non-alphanumeric characters
    
    return s == s[::-1]  # Check if the string is equal to its reverse

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
```

In this solution, we first convert the input string to lowercase using the `lower()` method. We then remove any non-alphanumeric characters using a generator expression. Finally, we compare the modified string with its reverse using slicing notation `[::-1]`. If they are equal, the function returns True, indicating that the string is a palindrome.