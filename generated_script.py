Problem: Given a string, write a function to check if the string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forwards and backwards. Ignore spaces, punctuation, and capitalization when checking for palindromes.

Example: 
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
The input string, "A man, a plan, a canal, Panama", is a palindrome when ignoring spaces, punctuation, and capitalization. When we remove all spaces and punctuation and convert all characters to lowercase, the resulting string is "amanaplanacanalpanama", which reads the same forwards and backwards.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

# Test the function with the example input
input_string = "A man, a plan, a canal, Panama"
print(is_palindrome(input_string))
```

Output:
True