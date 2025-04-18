Problem: Given a string, return the longest substring without repeating characters.

Explanation:
For example, given the string "abcabcbb", the longest substring without repeating characters is "abc", with a length of 3.

Solution in Python:

```python
def longest_substring(s):
    start = 0
    max_len = 0
    char_index = {}

    for end in range(len(s)):
        if s[end] in char_index:
            start = max(start, char_index[s[end]] + 1)
        char_index[s[end]] = end
        max_len = max(max_len, end - start + 1)

    return max_len

# Test the function with the example string
s = "abcabcbb"
print(longest_substring(s))  # Output: 3
```

This solution uses a sliding window technique to keep track of the longest substring without repeating characters. The `char_index` dictionary is used to store the index of the last occurrence of each character. The `start` variable is updated to the index after the last occurrence of the current character whenever a repeating character is encountered. The maximum length of the substring is continuously updated as the window slides through the string.