Problem:
Given a string, write a function that returns the first non-repeating character in the string. If all characters in the string are repeated, return None.

Example:
Input: "leetcode"
Output: "l"

Input: "loveleetcode"
Output: "v"

Input: "aabbcc"
Output: None

Solution:

```python
def first_non_repeating_character(s):
    char_count = {}
    
    # Count occurences of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

# Test the function
print(first_non_repeating_character("leetcode")) # Output: "l"
print(first_non_repeating_character("loveleetcode")) # Output: "v"
print(first_non_repeating_character("aabbcc")) # Output: None
```

Explanation:
- We first count the occurence of each character in the string using a dictionary.
- Then, we iterate through the string again and return the first character with a count of 1.
- If no such character is found, we return None.