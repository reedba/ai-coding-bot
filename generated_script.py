Problem: Given a string, return the first non-repeating character in the string. If there are no non-repeating characters, return None.

Example:
Input: "leetcode"
Output: "l"

Explanation:
In the input string "leetcode", the first non-repeating character is 'l'.

Solution in Python:

```python
def first_non_repeating_char(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

# Test the function
input_str = "leetcode"
print(first_non_repeating_char(input_str))  # Output: "l"
```

In this solution, we first create a dictionary `char_count` to store the count of each character in the input string. We then iterate through the string to populate the dictionary. Finally, we iterate through the input string again and return the first character with a count of 1, signifying that it is a non-repeating character. If no non-repeating characters are found, we return None.