Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Example:
Input: "A man, a plan, a canal, Panama"
Output: True (Palindrome)

Explanation:
To solve this problem, we can first remove all spaces, punctuation, and convert all characters to lowercase. Then we can compare the string with its reverse to see if they are equal.

Solution in Python:

```python
def is_palindrome(s):
    # Remove spaces and punctuation, and convert to lowercase
    s = ''.join(e.lower() for e in s if e.isalnum())
    
    # Compare the string with its reverse
    return s == s[::-1]

# Test the function
input_string = "A man, a plan, a canal, Panama"
print(is_palindrome(input_string))  # Output: True
```

This function `is_palindrome()` takes a string as input, removes all spaces and punctuation, converts all characters to lowercase, and then checks if the string is equal to its reverse. If it is, the function returns True indicating that the input string is a palindrome.