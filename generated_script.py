Problem: 

Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward (ignoring spaces, punctuation, and capitalization).

Input: 
String s

Output:
True if s is a palindrome, False otherwise

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
To check if a string is a palindrome, we can remove all the non-alphanumeric characters and convert the string to lowercase. Then we can compare the string to its reverse to see if they are equal.

Solution:
```python
def is_palindrome(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    return s == s[::-1]
    
# Test the function
test_string = "A man, a plan, a canal, Panama"
print(is_palindrome(test_string))  # Output: True
```