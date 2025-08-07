Problem: Given a string, write a Python function to check if it is a palindrome, ignoring spaces and capitalization. Return True if the string is a palindrome, and False otherwise.

Explanation:
- A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.
- In this problem, we will ignore spaces and capitalization when checking for palindromes. For example, "A man, a plan, a canal, Panama" should be considered a palindrome.

Solution:
```python
def is_palindrome(s):
    # Remove spaces and convert all characters to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
```

In the solution code:
1. We first clean the input string by removing spaces and converting all characters to lowercase using list comprehension.
2. Next, we check if the cleaned string is equal to its reverse using slicing.
3. The function returns True if the string is a palindrome and False otherwise.
4. We provide a few test cases to demonstrate the function's correctness.