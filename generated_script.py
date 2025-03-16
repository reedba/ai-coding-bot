Problem: 

Given a string of lowercase alphabets, write a Python function to find the longest substring with all unique characters.

Explanation:

For example, if input string is "abcabcbb", the output should be "abc" as it is the longest substring with unique characters.

Solution:

```python
def longest_unique_substring(s):
    start = 0
    max_length = 0
    seen = {}
    
    for i in range(len(s)):
        if s[i] in seen and start <= seen[s[i]]:
            start = seen[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        
        seen[s[i]] = i
        
    return s[start:start+max_length]

# Test the function
s = "abcabcbb"
print(longest_unique_substring(s))  # Output: "abc"
```

This function uses a sliding window approach to keep track of the longest substring with unique characters. It iterates through the string and updates the start index based on the current character's previous position in the seen dictionary. The max_length is updated accordingly. Finally, it returns the longest unique substring.