Sure! Here's a DSA problem related to strings and arrays:

Problem:
Given a list of strings, return the longest common prefix among them. If there is no common prefix, return an empty string.

Example:
Input: ["flower","flow","flight"]
Output: "fl"

Explanation:
In the above example, the common prefix among the strings "flower", "flow", and "flight" is "fl".

Solution in Python:

```
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Test the function with the example input
input_list = ["flower","flow","flight"]
output = longestCommonPrefix(input_list)
print(output)  # Output: "fl"
```

I hope this problem and solution helps you in your DSA learning journey! Let me know if you need further explanation or have any other questions.