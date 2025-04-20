Problem:

Given a string, write a Python function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.

Explanation:

To solve this problem, we can compare the original string with its reverse. If they are the same, then the string is a palindrome.

Solution:

```python
def is_palindrome(s):
    s = s.lower() # Convert string to lowercase for case-insensitivity
    s = ''.join(e for e in s if e.isalnum()) # Remove non-alphanumeric characters
    
    return s == s[::-1] # Check if the string is the same forwards and backwards

# Test the function
input_string = "A man, a plan, a canal, Panama"
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
```

In this solution, we first convert the input string to lowercase and remove non-alphanumeric characters using a list comprehension. Then, we compare the original string with its reverse (using slicing notation `s[::-1]`) to determine if the string is a palindrome.