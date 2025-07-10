Problem: Given a string, write a Python function to return the length of the longest substring without repeating characters.

Explanation: We are given a string and we need to find the length of the longest substring within that string that does not contain any repeating characters. For example, in the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3.

Solution:
```python
def longest_substring(s):
    n = len(s)
    if n == 0:
        return 0
    
    char_index = {} 
    max_length = 0
    start = 0
    
    for end in range(n):
        if s[end] in char_index:
            start = max(start, char_index[s[end]] + 1)
        
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Test the function
print(longest_substring("abcabcbb")) # Output: 3
print(longest_substring("bbbbb")) # Output: 1
print(longest_substring("pwwkew")) # Output: 3
```

In this solution, we use a dictionary to store the index of each character as we iterate through the string. We also maintain a `start` variable that keeps track of the start index of the current substring without repeating characters. We update the `start` index whenever we encounter a repeating character. At each step, we calculate the length of the current substring and update `max_length` accordingly. Finally, we return the `max_length` as the result.