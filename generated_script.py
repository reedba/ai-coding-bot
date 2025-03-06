Problem:
Given a string, find the first non-repeating character and return its index. If there is no non-repeating character, return -1.

Example:
Input: "leetcode"
Output: 0 (The first non-repeating character is 'l' at index 0)

Input: "loveleetcode"
Output: 2 (The first non-repeating character is 'v' at index 2)

Solution in Python:

```python
def firstUniqChar(s: str) -> int:
    char_count = {}
    
    # Count the frequency of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the index of the first non-repeating character
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i
    
    return -1

# Test the function with examples
print(firstUniqChar("leetcode")) # Output: 0
print(firstUniqChar("loveleetcode")) # Output: 2
```

Explanation:
- We first create a dictionary `char_count` to store the frequency of each character in the string.
- We iterate through the string and update the frequency count for each character.
- We then iterate through the string again to find the index of the first character with a frequency of 1 (non-repeating character).
- If a non-repeating character is found, we return its index. If no non-repeating character is found, we return -1.