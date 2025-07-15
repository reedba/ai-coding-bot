Problem: Given a string, find the first non-repeating character and return its index. If all characters in the string are repeated, return -1.

Example:
Input: "leetcode"
Output: 0 (The first non-repeating character is 'l' at index 0)
 
Input: "loveleetcode"
Output: 2 (The first non-repeating character is 'v' at index 2)

Explanation:
To solve this problem, we can loop through the string and create a dictionary to store the frequency of each character. After building the frequency dictionary, we can loop through the string again and check if the frequency of the character is 1. If we find a character with frequency 1, we return its index. If no such character is found, we return -1.

Python Solution:
```python
def first_non_repeating_char(s):
    char_freq = {}
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    for i in range(len(s)):
        if char_freq[s[i]] == 1:
            return i

    return -1

# Test the function
print(first_non_repeating_char("leetcode")) # Output: 0
print(first_non_repeating_char("loveleetcode")) # Output: 2
``` 

This solution has a time complexity of O(n) where n is the length of the input string `s`, as we are looping through the string twice in two separate iterations.