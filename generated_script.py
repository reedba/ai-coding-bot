Problem: Given a string, write a function to check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

Explanation: To check if a string is a palindrome, we can compare the characters at the beginning and end of the string, moving towards the center. If the characters match at each position, the string is a palindrome. We can ignore spaces, punctuation, and capitalization when comparing the characters.

Solution in Python:

```python
def is_palindrome(s):
    # Convert the string to lowercase and remove spaces and punctuation
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    
    # Compare characters from beginning and end of the string
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    
    return True

# Test the function with some examples
print(is_palindrome("A man, a plan, a canal, Panama")) # True
print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False
```

In this solution, we first convert the input string to lowercase and remove any non-alphanumeric characters using list comprehension. Then, we iterate through the characters from the beginning and end of the string simultaneously, comparing them at each position. If any pair of characters do not match, we return False. If we reach the middle of the string without finding any mismatches, we return True indicating that the string is a palindrome.