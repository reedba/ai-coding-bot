Problem: Given a string, create a function that returns the longest substring without repeating characters.

Example:
Input: "abcabcbb"
Output: "abc"

Explanation:
In the input string "abcabcbb", the longest substring without repeating characters is "abc".

Solution in Python:

```python
def longest_substring(s):
    if not s:
        return 0
    
    start = 0
    max_length = 0
    seen = {}
    
    for end in range(len(s)):
        if s[end] in seen and start <= seen[s[end]]:
            start = seen[s[end]] + 1
        else:
            max_length = max(max_length, end - start + 1)
        
        seen[s[end]] = end
    
    return max_length

# Test the function with the example
input_string = "abcabcbb"
output = longest_substring(input_string)
print(output) # Output: 3 (corresponding to "abc")
```

This function uses a sliding window approach to keep track of the longest substring without repeating characters. It iterates through the input string `s` and uses a dictionary `seen` to store the index of each character seen so far.

The `start` pointer is used to keep track of the start of the current substring without repeating characters, and `max_length` is updated whenever a longer substring is found. If a repeating character is encountered, the `start` pointer is moved to the index of the previous occurrence of the character + 1.

Overall, the function has a time complexity of O(n) where n is the length of the input string `s`.