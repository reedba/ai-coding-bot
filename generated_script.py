Problem: Given a string s containing lowercase letters, return the first non-repeating character in the string. If there are no non-repeating characters, return '_'.

Example:
Input: s = "leetcode"
Output: "l"

Explanation:
In the given string "leetcode", the first non-repeating character is 'l' as it only appears once in the string.

Solution in Python:

```python
def first_non_repeating_char(s):
    letter_count = {}
    
    # Count the occurrence of each character in the string
    for char in s:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
            
    # Find the first non-repeating character
    for char in s:
        if letter_count[char] == 1:
            return char
    
    return "_"

# Test the function with the example input
s = "leetcode"
print(first_non_repeating_char(s))  # Output: "l"
```

This solution uses a dictionary to store the count of each character in the string and then iterates through the string to find the first non-repeating character.