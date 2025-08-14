Problem:

Given a string, write a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Example:
Input: "A man, a plan, a canal: Panama"
Output: True

Input: "racecar"
Output: True

Input: "hello"
Output: False

Explanation:
To solve this problem, we can first remove all non-alphanumeric characters and convert the string to lowercase. Then, we can use two pointers approach to check if the string is a palindrome. Move the pointers towards the center of the string while comparing the characters at each position.

Solution in Python:

```python
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()   # remove non-alphanumeric and convert to lowercase
    left, right = 0, len(s) - 1   # initialize two pointers
    
    while left < right:
        if s[left] != s[right]:   # if characters at left and right pointers are not equal
            return False
        left += 1
        right -= 1
    
    return True

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("racecar"))   # Output: True
print(is_palindrome("hello"))   # Output: False
```

This function first sanitizes the input string by removing non-alphanumeric characters and converting it to lowercase. Then, it uses a two pointers approach to traverse the string and check for palindrome property. 
The time complexity of this solution is O(n) where n is the length of the input string.