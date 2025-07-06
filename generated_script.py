Problem: Given a string, return the first non-repeating character in the string. If there are no non-repeating characters, return -1.

Example:
Input: "hello"
Output: "h"

Input: "leetcode"
Output: "l"

Input: "aabbcc"
Output: -1

Explanation:
To solve this problem, we can create a dictionary to store the count of each character in the input string. Then, we can iterate through the string again and check if the count of the character in the dictionary is equal to 1. If we find such character, we return it as the first non-repeating character.

Solution in Python:

```python
def firstNonRepeatingChar(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in s:
        if char_count[char] == 1:
            return char
    
    return -1

# Test cases
print(firstNonRepeatingChar("hello")) # Output: "h"
print(firstNonRepeatingChar("leetcode")) # Output: "l"
print(firstNonRepeatingChar("aabbcc")) # Output: -1
```