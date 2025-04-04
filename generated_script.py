Problem: Given a string, write a function to return the first non-repeating character in the string. If all characters in the string are repeating, return -1.

Explanation:
- We need to iterate through the string and keep track of the frequency of each character.
- After that, we can iterate through the string again to find the first character with a frequency of 1.

Solution in Python:

```python

def firstNonRepeatingChar(s):
    char_freq = {}
    
    # Count the frequency of each character in the string
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Find the first non-repeating character
    for char in s:
        if char_freq[char] == 1:
            return char
    
    return -1

# Test the function
print(firstNonRepeatingChar("leetcode")) # Output: "l"
print(firstNonRepeatingChar("loveleetcode")) # Output: "v"
print(firstNonRepeatingChar("aabbcc")) # Output: -1

```

In this solution, we first count the frequency of each character in the input string `s`. Then, we iterate through the string again to find the first character with a frequency of 1 and return it. If all characters are repeating, we return -1.