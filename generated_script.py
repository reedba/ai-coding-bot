Problem: Given a string s, return the length of the longest substring without repeating characters.

Example:

Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc", which has a length of 3.

Solution (Python):

```python
def lengthOfLongestSubstring(s: str) -> int:
    start = maxLength = 0
    usedChars = {}

    for i, char in enumerate(s):
        if char in usedChars and start <= usedChars[char]:
            start = usedChars[char] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChars[char] = i

    return maxLength

# Test the function
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # Output: 3
```