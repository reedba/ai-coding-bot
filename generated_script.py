Problem: Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
To solve this problem, we can first remove all non-alphanumeric characters from the input string and convert it to lowercase. Then we can compare the string with its reverse to check if it is a palindrome.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()  # remove non-alphanumeric characters and convert to lowercase
    return s == s[::-1]  # check if the string is equal to its reverse

# Test the function with the given example
input_str = "A man, a plan, a canal, Panama"
print(is_palindrome(input_str))  # Output: True
```

This function takes a string as input, removes all non-alphanumeric characters and converts it to lowercase. It then checks if the modified string is equal to its reverse, returning True if it is a palindrome and False if it is not.