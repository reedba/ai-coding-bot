Problem: Given a string, return the first non-repeating character in the string. If all characters in the string are repeating, return -1.

Example:

Input: "leetcode"
Output: "l"

Input: "loveleetcode"
Output: "v"

Input: "aabbcc"
Output: -1

Explanation: In the first example, "l" is the first non-repeating character in the string "leetcode". In the second example, "v" is the first non-repeating character in the string "loveleetcode". In the third example, all characters in the string "aabbcc" are repeating, so the output is -1.

Solution in Python:

```python
def first_non_repeating_char(s):
    char_count = {}
    
    # count the occurrences of each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    
    return -1

# test cases
print(first_non_repeating_char("leetcode")) # Output: "l"
print(first_non_repeating_char("loveleetcode")) # Output: "v"
print(first_non_repeating_char("aabbcc")) # Output: -1

```

Explanation: In the solution, we first count the occurrences of each character in the given string using a dictionary. Then, we iterate through the string to find the first non-repeating character by checking the count of each character in the dictionary. If we find a character with a count of 1, we return that character as the first non-repeating character. If no such character exists, we return -1.