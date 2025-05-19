Problem: Given a string, check if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward (ignoring spaces and punctuation).

Example:
Input: "racecar"
Output: True
Explanation: "racecar" is a palindrome as it reads the same forwards and backwards.

Input: "hello"
Output: False
Explanation: "hello" is not a palindrome as it does not read the same forwards and backwards.

Solution in Python:

```python
def is_palindrome(s):
    # Preprocess the input string by removing spaces and converting to lowercase
    s = ''.join(filter(str.isalnum, s.lower()))
    
    # Check if the preprocessed string is equal to its reverse
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("Hello"))    # False
print(is_palindrome("A man a plan a canal Panama"))  # True
```

Explanation:
1. The function `is_palindrome()` preprocesses the input string by removing spaces and converting all characters to lowercase using `filter()` and `lower()` methods.
2. It then checks if the preprocessed string is equal to its reverse using slicing (`[::-1]`).
3. If the preprocessed string is equal to its reverse, the function returns True, indicating that the input string is a palindrome. Otherwise, it returns False.
4. Test cases demonstrate the function's correctness for various input strings.