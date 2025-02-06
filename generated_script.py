Sure, here's a DSA problem related to strings and arrays:

Problem:
Given a string, write a function in Python that returns the longest substring without repeating characters.

Example:
Input: "abcabcbb"
Output: "abc"

Explanation:
In the given input string "abcabcbb", the longest substring without repeating characters is "abc", as it does not contain any repeating characters.

Solution:
```python
def longest_substring(input_str):
    seen = {}
    start = 0
    max_len = 0
    max_start = 0
    
    for i, char in enumerate(input_str):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        if i - start + 1 > max_len:
            max_len = i - start + 1
            max_start = start
    
    return input_str[max_start:max_start + max_len]

# Test the function with the given example
input_str = "abcabcbb"
print(longest_substring(input_str))  # Output: "abc"
```

In this solution, we are using a dictionary `seen` to keep track of the index of each character we have seen so far. We also use two pointers `start` and `max_start` to keep track of the starting index of the current substring without repeating characters and the starting index of the longest substring found so far. We iterate over the input string, updating the `start` pointer when we encounter a repeating character, and updating the `max_len` and `max_start` if we find a longer substring without repeating characters. Finally, we return the longest substring found.