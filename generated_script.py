Problem:
Create a function that takes in a list of strings and returns the longest common prefix among all the strings. If there is no common prefix, return an empty string.

Explanation:
The common prefix is the longest string that is a prefix of all the strings in the list. For example, for the input ["flower", "flour", "flask"], the common prefix is "fl".

Solution in Python:

```python
def longest_common_prefix(strs):
    if not strs:
        return ""

    shortest_str = min(strs, key=len)
    
    for i, char in enumerate(shortest_str):
        for string in strs:
            if string[i] != char:
                return shortest_str[:i]
    
    return shortest_str

# Test the function
print(longest_common_prefix(["flower", "flour", "flask"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))  # Output: ""
print(longest_common_prefix([]))  # Output: ""
```

In this solution, we first find the shortest string in the list. Then, we iterate through each character of the shortest string and compare it with the corresponding characters in other strings. If we find a mismatch, we return the prefix up to that point. If no mismatches are found, we return the entire shortest string as the common prefix.