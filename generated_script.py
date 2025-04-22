Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forwards and backwards. The function should return True if the input string is a palindrome, and False otherwise.

Explanation:
We can solve this problem by comparing the original string with its reverse. If the two strings are the same, then it is a palindrome.

Solution:

```python
def is_palindrome(s):
    # Remove all non-alphanumeric characters and convert the string to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test the function
print(is_palindrome("A man, a plan, a canal: Panama")) # Output: True
print(is_palindrome("race a car")) # Output: False
```

In the above solution, we first remove all non-alphanumeric characters and convert the string to lowercase using list comprehension. Then, we check if the modified string is equal to its reverse using slicing (s[::-1]). If they are equal, we return True, indicating that the input string is a palindrome. Otherwise, we return False.