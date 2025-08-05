Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
In the above example, the input string "A man, a plan, a canal, Panama" is a palindrome when we ignore spaces, punctuation, and capitalization. When we remove the spaces, punctuation, and capitalize all characters, we get "amanaplanacanalpanama", which reads the same forward and backward.

Solution:
```python
def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower() # Remove non-alphanumeric characters and convert to lowercase
    return s == s[::-1]

# Test the function
input_str = "A man, a plan, a canal, Panama"
print(is_palindrome(input_str))  # Output: True
```

In the solution, we first remove all non-alphanumeric characters from the input string and convert it to lowercase. Then, we check if the modified string is equal to its reverse. If they are equal, then the input string is a palindrome and we return True.