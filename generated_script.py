Problem:
Given a string containing only lowercase English letters, write a function to find the longest substring with at most K distinct characters.

Example:
Input: s = "abcbbbbcccbdddadacb", K = 2
Output: 10
Explanation: The longest substring with at most 2 distinct characters is "bcbbbbcccb".

Python Solution:
```python
def longest_substring(s, K):
    if not s:
        return 0

    left, right = 0, 0
    max_length = 0
    char_count = {}
    
    while right < len(s):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        while len(char_count) > K:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
        right += 1
    
    return max_length

s = "abcbbbbcccbdddadacb"
K = 2
print(longest_substring(s, K))
```

Explanation:
- Initialize left pointer, right pointer, maximum length, and a dictionary to store the count of each character.
- Iterate through the string using the right pointer and update the character count in the dictionary.
- Move the left pointer to shrink the window if the number of distinct characters exceeds K.
- Update the maximum length with the current window size.
- Return the maximum length of the substring with at most K distinct characters.