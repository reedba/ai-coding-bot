Problem:
Given a string, find the first non-repeating character and return its index. If there is no non-repeating character, return -1.

Example:
Input: "leetcode"
Output: 0

Explanation:
In the input string "leetcode", the first non-repeating character is 'l' at index 0.

Solution in Python:

```python
def firstNonRepeatingChar(s):
    char_count = {}
    
    # Count the occurrences of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first non-repeating character and return its index
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i
    
    return -1

# Test the function with the example input
input_str = "leetcode"
index = firstNonRepeatingChar(input_str)
print(index)
```

This solution uses a dictionary to store the count of each character in the string. Then, it iterates through the string to find the first non-repeating character and returns its index. If there is no non-repeating character, it returns -1.