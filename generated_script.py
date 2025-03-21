Problem:

Given a string, write a function that returns the first non-repeating character in the string. If there are no non-repeating characters, return -1.

Example:
Input: "hello"
Output: "h"

Input: "leetcode"
Output: "l"

Input: "aaaaa"
Output: -1

Explanation:
In the first example, the first non-repeating character is "h".
In the second example, the first non-repeating character is "l".
In the third example, all characters are repeating, so there is no non-repeating character.

Solution in Python:

```python
def first_non_repeating_char(s):
    char_count = {}
    
    # Count occurrences of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    
    return -1

# Test cases
print(first_non_repeating_char("hello"))  # Output: "h"
print(first_non_repeating_char("leetcode"))  # Output: "l"
print(first_non_repeating_char("aaaaa"))  # Output: -1
```

This solution first creates a dictionary to store the count of each character in the input string. Then, it loops through the string again to find the first character with a count of 1, indicating that it is a non-repeating character. If no such character is found, it returns -1.