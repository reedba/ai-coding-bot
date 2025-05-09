Problem:
Given a list of strings, write a function to return the longest common prefix among them. If there is no common prefix, return an empty string.

Example:
Input: ["flower","flow","flight"]
Output: "fl"

Explanation:
In the given list of strings, "fl" is the longest common prefix.

Solution in Python:

```python
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Test the function
input_strings = ["flower","flow","flight"]
print(longest_common_prefix(input_strings)) # Output: "fl"
```

In this solution, we first check if the input list is empty. Then, we initialize the prefix as the first string in the list. We iterate through the list of strings and compare the prefix with each string. If the prefix does not match the beginning of a string, we reduce the prefix by one character. This process continues until we find the longest common prefix among all the strings.