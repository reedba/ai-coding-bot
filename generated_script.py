Problem: 
Given a string s, find the length of the longest substring without repeating characters.

Explanation:
For example, given the input string "abcabcbb", the longest substring without repeating characters is "abc", which has a length of 3. Another example would be the input string "pwwkew", the longest substring without repeating characters is "wke", which has a length of 3.

Solution in Python:
```python
def longest_substring_without_repeating_chars(s):
    n = len(s)
    start = 0
    max_length = 0
    char_index = {}

    for i in range(n):
        if s[i] in char_index:
            start = max(start, char_index[s[i]] + 1)
        char_index[s[i]] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Test the function with examples
print(longest_substring_without_repeating_chars("abcabcbb"))  # Output: 3
print(longest_substring_without_repeating_chars("pwwkew"))    # Output: 3
```

This solution uses a sliding window technique to keep track of the current substring without repeating characters. We maintain a dictionary `char_index` to store the most recent index of each character we have seen in the string `s`. The `start` variable is used to keep track of the start of the current substring without repetition, and `max_length` stores the length of the longest such substring found so far.