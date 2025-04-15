Problem: 
Given a string, return the first non-repeating character in the string. If there are no non-repeating characters, return -1.

Example:
Input: "leetcode"
Output: "l"

Input: "loveleetcode"
Output: "v"

Input: "aabbcc"
Output: -1

Explanation:
To solve this problem, we can iterate through the string and use a dictionary to keep track of the frequency of each character. After populating the dictionary, we can iterate through the string again and return the first character with a frequency of 1.

Solution in Python:

```python
def firstNonRepeatingChar(s):
    count = {}
    
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char in s:
        if count[char] == 1:
            return char
    
    return -1

# Test cases
print(firstNonRepeatingChar("leetcode")) # Output: "l"
print(firstNonRepeatingChar("loveleetcode")) # Output: "v"
print(firstNonRepeatingChar("aabbcc")) # Output: -1
```