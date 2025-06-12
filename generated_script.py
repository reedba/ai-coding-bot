Problem:

Given a string, return the first non-repeating character in the string.

Explanation:

You are given a string of lowercase English letters. You need to find and return the first non-repeating character in the string. A non-repeating character is a character that appears only once in the string. If no such character exists, return an empty string.

For example, given the input "leetcode", the output should be "l" because 'l' is the first character that does not repeat in the string.

Solution in Python:

```python
def first_non_repeating_character(s):
    char_count = {}

    # Count the frequency of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char

    return ""

# Test the function
input_str = "leetcode"
output = first_non_repeating_character(input_str)
print(output)  # Output: l
```

In this solution, we first count the frequency of each character in the input string using a dictionary. Then, we iterate through the string again and return the first character that has a frequency of 1. If no such character is found, we return an empty string.