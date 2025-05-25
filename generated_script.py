Problem: Given a list of strings, write a function to find the longest common prefix amongst all strings. If there is no common prefix, return an empty string.

Example:
Input: ["flower", "flow", "flight"]
Output: "fl"

Explanation: The longest common prefix amongst the strings "flower", "flow", and "flight" is "fl".

Solution in Python:

```python
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[0: len(prefix) - 1]
            if len(prefix) == 0:
                return ""
    
    return prefix

# Test the function
input_strings = ["flower", "flow", "flight"]
print(longestCommonPrefix(input_strings))  # Output: "fl"
```

This function first initializes the prefix as the first string in the list. Then, it checks each string in the list to see if the prefix is a substring of that string. If not, it gradually shortens the prefix until it finds the common prefix. Finally, it returns the longest common prefix found among all strings.