Problem: Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. Ignore capitalization, punctuation, and spacing when determining if a string is a palindrome.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
In the given string, if we ignore all the non-alphanumeric characters and spaces, we get "amanaplanacanalpanama" which is a palindrome when read in reverse.

Solution in Python:
```python
def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower() # Remove non-alphanumeric characters and convert to lowercase
    return s == s[::-1] # Check if the string is equal to its reverse
    
# Test the function
input_string = "A man, a plan, a canal, Panama"
print(is_palindrome(input_string)) # Output: True
```