Problem: Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc", which has a length of 3.

Solution (Python):

```python
def longest_substring(s):
    start = 0
    max_length = 0
    char_map = {}

    for end in range(len(s)):
        if s[end] in char_map:
            start = max(start, char_map[s[end]] + 1)
        
        char_map[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# Test the function
s = "abcabcbb"
print(longest_substring(s))  # Output: 3
```

Explanation:
- We use a two-pointer approach, with `start` and `end` pointers to keep track of the current substring we are checking.
- We also use a dictionary `char_map` to store the index of the last occurrence of each character.
- If a character is already in `char_map`, we update the `start` pointer to the maximum of its current position and the position stored in `char_map` (plus 1).
- We update `char_map` with the current index of the character.
- At each step, we calculate the length of the current substring and update `max_length` if necessary.
- Finally, we return the length of the longest substring without repeating characters.