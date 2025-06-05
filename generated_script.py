Problem:
Given a list of strings, write a function that returns the longest common prefix among all strings. If there is no common prefix, return an empty string.

Example:
Input: ["leetcode", "leed", "lee"]
Output: "lee"

Explanation:
In the given list of strings, the longest common prefix among all strings is "lee".

Solution in Python:

```python
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for string in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
            i += 1
        prefix = prefix[:i]
    
    return prefix

# Test the function
input_list = ["leetcode", "leed", "lee"]
print(longestCommonPrefix(input_list))  # Output: "lee"
```

In this solution, we first check if the input list is empty and return an empty string if so. We then initialize the `prefix` variable to the first string in the list. We iterate through the remaining strings in the list and compare each character of the prefix with the corresponding character in the current string. If the characters match, we increment the index `i`, otherwise, we break out of the loop. Finally, we return the `prefix` string which contains the longest common prefix among all strings.