Problem: Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Ignore case, spaces, and punctuation when checking for palindromes.

Example:
Input: "A man, a plan, a canal, Panama"
Output: True

Explanation:
In this example, the input string is "A man, a plan, a canal, Panama". If we ignore case, spaces, and punctuation, the string becomes "amanaplanacanalpanama", which is a palindrome.

Solution in Python:
```python
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()  # Remove non-alphanumeric characters and convert to lowercase
    return s == s[::-1]  # Check if the string is equal to its reverse

# Test the function with the example
input_string = "A man, a plan, a canal, Panama"
print(is_palindrome(input_string))  # Output: True
```

In this solution, we first remove all non-alphanumeric characters and convert the string to lowercase using list comprehension and the `filter()` function. Then, we check if the modified string is equal to its reverse by comparing it to `s[::-1]` which is the reverse of the string. Finally, we return True if the string is a palindrome and False otherwise.