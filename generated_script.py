Problem: Write a function in Python that takes in a string as input and returns the length of the longest substring without repeating characters.

Explanation: Given a string, we need to find the length of the longest substring that does not contain any repeating characters. For example, for the input string "abcabcbb", the longest substring without repeating characters is "abc" and the length of this substring is 3.

Solution:

```python
def length_of_longest_substring(s):
    if not s:
        return 0
    
    max_length = 0
    start = 0
    seen = {}
    
    for end in range(len(s)):
        if s[end] in seen:
            start = max(start, seen[s[end]] + 1)
        
        seen[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Test the function
input_string = "abcabcbb"
print(length_of_longest_substring(input_string))  # Output: 3
```

In this solution, we use a sliding window approach to traverse the string and keep track of the start and end index of the current substring without repeating characters. We use a dictionary `seen` to store the index of the last occurrence of each character encountered. If we encounter a character that is already in the `seen` dictionary, we update the `start` index to be the maximum of the current `start` index and the index of the repeating character plus 1. We update the `max_length` based on the length of the current substring without repeating characters. Finally, we return the `max_length` as the result.