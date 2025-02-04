Problem: Given a string, find the first non-repeating character and return its index. If no unique character exists, return -1.

Example:
Input: "leetcode"
Output: 0

Input: "loveleetcode"
Output: 2

Explanation:
In the first example, the only non-repeating character is 'l' at index 0.
In the second example, the first non-repeating character is 'v' at index 2.

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
    
    # find the index of the first non-repeating character
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i
    
    return -1

# Test the function with the given examples
print(firstUniqChar("leetcode"))  # Output: 0
print(firstUniqChar("loveleetcode"))  # Output: 2
```

This solution uses a dictionary to keep track of the frequency of each character in the string. Then, it iterates through the string to find the index of the first non-repeating character by checking the frequency in the dictionary. Finally, it returns the index or -1 if no unique character is found.