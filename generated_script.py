Problem: Given a string, find the longest substring with non-repeating characters.

Explanation: 
Write a function named `longest_substring` that takes a string as input and returns the length of the longest substring with non-repeating characters. For example, given the input "abcabcbb", the longest substring with non-repeating characters is "abc" which has a length of 3. 

Solution in Python:

```python
def longest_substring(s):
    seen = {}
    start = 0
    max_length = 0
    
    for i in range(len(s)):
        if s[i] in seen:
            start = max(start, seen[s[i]] + 1)
        seen[s[i]] = i
        max_length = max(max_length, i - start + 1)
    
    return max_length

# Test the function
input_str = "abcabcbb"
print(longest_substring(input_str))  # Output: 3
```

In the solution, we use a dictionary `seen` to store the index of each character we have seen. We also maintain a `start` pointer that marks the start of the current substring with non-repeating characters. As we iterate through the string, we update the `start` pointer whenever we encounter a repeated character, and update the `max_length` whenever we find a longer substring. Finally, we return the `max_length` as the result.