Problem:

Given a string, return the first non-repeating character in it and its index. If it doesn't exist, return -1.

Example:
Input: "hello"
Output: ('h', 0)

Input: "leetcode"
Output: ('l', 1)

Input: "loveleetcode"
Output: ('v', 2)

Explanation:

To solve this problem, we can iterate through the string and store the count of each character in a dictionary. Then, we can iterate through the string again and find the first character with a count of 1.

Solution in Python:

def first_non_repeating_char(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return (char, i)
    
    return -1

# Test cases
print(first_non_repeating_char("hello"))  # Output: ('h', 0)
print(first_non_repeating_char("leetcode"))  # Output: ('l', 1)
print(first_non_repeating_char("loveleetcode"))  # Output: ('v', 2)