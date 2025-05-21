Problem: 

Given a list of strings, find the longest common prefix among them. If there is no common prefix, return an empty string.

Example:
Input: ["flower", "flow", "flight"]
Output: "fl"

Explanation:
The common prefix among the strings "flower", "flow", and "flight" is "fl". 

Solution in Python:

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while prefix:
            if s.startswith(prefix):
                break
            prefix = prefix[:-1]
    
    return prefix

# Test the function with example input
input_list = ["flower", "flow", "flight"]
print(longest_common_prefix(input_list))  # Output: "fl"
```

This function takes a list of strings as input and iterates over each string to find the longest common prefix among them. It does this by initially setting the prefix to the first string in the list, then iterates over the rest of the strings checking if they start with the prefix. If a string does not start with the prefix, the function shortens the prefix by removing the last character and continues until a common prefix is found.