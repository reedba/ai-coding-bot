Problem:

Given a list of strings, write a function to find and return the longest common prefix among all strings. If there is no common prefix, return an empty string.

Example:
Input: ["flower", "flow", "flight"]
Output: "fl"

Explanation:
In the given list of strings, the longest common prefix among all strings is "fl".

Solution:

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    min_len = min(map(len, strs))
    
    for i in range(min_len):
        for j in range(1, len(strs)):
            if strs[j][i] != strs[0][i]:
                return strs[0][:i]
    
    return strs[0][:min_len]

# Test the function
input_strings = ["flower", "flow", "flight"]
print(longest_common_prefix(input_strings))  # Output: "fl"
```

In this solution, we iterate through the list of strings and compare each character at the same index in all strings. We stop the comparison as soon as we find a character that doesn't match. The longest common prefix is then the substring up to that point. If all characters match up to the minimum length of all strings, we return the entire string at index 0.