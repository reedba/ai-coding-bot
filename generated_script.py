Problem: Write a function that takes in a string and returns the first non-repeating character in the string. If all characters are repeating, return -1.

Explanation:
We can solve this problem by creating a dictionary to store the frequency of each character in the string. Then, we iterate through the string and check if the frequency of the character is 1. If we find a character with frequency 1, we return that character. If no character has frequency 1, we return -1.

Solution in Python:

```python
def first_non_repeating_char(s):
    freq = {}
    
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    for char in s:
        if freq[char] == 1:
            return char
    
    return -1

# Test the function
print(first_non_repeating_char("leetcode"))  # Output: 'l'
print(first_non_repeating_char("hello"))     # Output: 'h'
print(first_non_repeating_char("aabbcc"))    # Output: -1
```

This function first creates a dictionary `freq` to store the frequency of characters in the input string `s`. It then iterates through the string to populate the dictionary. Finally, it iterates through the string again to find the first non-repeating character and returns it, or -1 if no such character is found.