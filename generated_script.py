Problem:
Given a string s, return the length of the longest substring containing only unique characters.

Example:
Input: s = "abcabcbb"
Output: 3 (The longest substring without repeating characters is "abc", which has a length of 3)

Input: s = "bbbbb"
Output: 1 (The longest substring without repeating characters is "b", which has a length of 1)

Solution in Python:

```python
def longest_unique_substring(s):
    n = len(s)
    max_length = 0
    start = 0
    char_map = {}
    
    for i in range(n):
        if s[i] in char_map:
            start = max(start, char_map[s[i]] + 1)
        char_map[s[i]] = i
        max_length = max(max_length, i - start + 1)
    
    return max_length

# Test the function with given examples
print(longest_unique_substring("abcabcbb"))  # Output: 3
print(longest_unique_substring("bbbbb"))  # Output: 1
```

Explanation:
- The function `longest_unique_substring` takes a string `s` as input and returns the length of the longest substring without repeating characters.
- We maintain a `start` index to keep track of the start of the current substring and a `char_map` dictionary to store the index of the last occurrence of each character.
- We iterate through the string `s`, updating the `start` index if we encounter a repeating character. We also update the `char_map` with the current character's index.
- At each iteration, we update `max_length` with the maximum length of the current substring without repeating characters.
- Finally, we return the `max_length` as the result.