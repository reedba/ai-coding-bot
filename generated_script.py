Problem: Given a string, determine if it is a palindrome.

Explanation: A palindrome is a string that reads the same forwards and backwards. For example, "racecar" is a palindrome. Your task is to write a function that takes a string as input and returns True if it is a palindrome, and False otherwise. Ignore spaces, punctuation, and capitalization when checking for palindromes.

Solution:

```python
def is_palindrome(s):
    s = s.lower() # Convert the string to lowercase
    s = ''.join(filter(str.isalnum, s)) # Remove non-alphanumeric characters
    return s == s[::-1] # Check if the string is equal to its reverse

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
```

In this solution, we first convert the input string to lowercase using the `lower()` method. We then remove all non-alphanumeric characters using the `filter()` function and `isalnum()` method. Finally, we check if the modified string is equal to its reverse using slicing (`[::-1]`). If the two strings are equal, we return True, indicating that the input string is a palindrome.