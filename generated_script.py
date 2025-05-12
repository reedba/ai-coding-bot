Problem: Given a string, return the first non-repeating character in that string. If there are no non-repeating characters, return -1.

Explanation: In this problem, we are asked to find the first non-repeating character in a given string. A non-repeating character is a character that appears only once in the string.

Solution:

```python
def first_non_repeating_char(s):
    freq = {}
    
    # Count frequency of each character in the string
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # Find the first non-repeating character
    for char in s:
        if freq[char] == 1:
            return char
    
    return -1

# Test the function
s = "leetcode"
print(first_non_repeating_char(s))  # Output: "l"

s = "loveleetcode"
print(first_non_repeating_char(s))  # Output: "v"

s = "aabbcc"
print(first_non_repeating_char(s))  # Output: -1
```

In this solution, we first create a dictionary `freq` to store the frequency of each character in the input string `s`. Then, we iterate over the string to find the first character with a frequency of 1, which indicates a non-repeating character. If no such character is found, we return -1.