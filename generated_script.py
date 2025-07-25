Problem: Given a string s, write a function to return the first non-repeating character in the string. If there are no non-repeating characters, return -1.

Example:
Input: s = "leetcode"
Output: "l"

Explanation:
In the given string "leetcode", the first non-repeating character is 'l', as it appears only once in the string.

Solution in Python:

```python
def firstNonRepeatingChar(s):
    char_count = {}
    
    # Count the frequency of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    
    return -1

# Test the function with the example input
s = "leetcode"
print(firstNonRepeatingChar(s))  # Output: l
```

Explanation:
- We first create a dictionary `char_count` to store the frequency of each character in the input string `s`.
- We then iterate through the string to count the frequency of each character.
- Finally, we iterate through the string again to find the first character with a count of 1, which indicates it is a non-repeating character.
- If no non-repeating character is found, we return -1.