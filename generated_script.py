Problem:

Given a string, find the longest substring without repeating characters.

Example:

Input: "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc", which has a length of 3.

Solution:

```python
def longest_substring(s):
    n = len(s)
    if n == 0:
        return 0

    max_len = 0
    start = 0
    char_index = {}

    for i in range(n):
        if s[i] in char_index:
            start = max(start, char_index[s[i]] + 1)
        char_index[s[i]] = i
        max_len = max(max_len, i - start + 1)

    return max_len

# Test the function
print(longest_substring("abcabcbb")) # Output: 3
```

Explanation:
- We initialize variables `max_len` and `start` to track the maximum length of substring without repeating characters and the starting index of the current substring.
- We also initialize a dictionary `char_index` to store the index of each character in the string.
- We iterate through the string and update the `start` index whenever we encounter a repeating character (i.e., the character is already in the `char_index` dictionary).
- We update the `max_len` by calculating the length of the current substring without repeating characters.
- Finally, we return the `max_len` as the result.