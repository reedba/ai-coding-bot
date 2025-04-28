Problem:
Given an array of strings, write a function that returns the longest common prefix among all strings. If there is no common prefix, return an empty string.

Example:
Input: ["flower", "flow", "flight"]
Output: "fl"

Explanation:
In the above example, the longest common prefix among all strings is "fl".

Solution in Python:

```python
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Sort the array of strings
    strs.sort()
    
    # Find the common prefix between the first and last string
    prefix = ""
    for c in strs[0]:
        if strs[-1].startswith(prefix + c):
            prefix += c
        else:
            break
    
    return prefix

# Test the function with example input
input_list = ["flower", "flow", "flight"]
print(longestCommonPrefix(input_list))
```

Output:
```
fl
``` 

In the above solution, we first sort the array of strings to make it easier to compare the first and last strings to find the common prefix. We then iterate through the characters of the first string and check if the prefix + character is a prefix of the last string. If it is, we add the character to the prefix, if not, we break out of the loop and return the prefix found so far.