Problem:
Given a string, return the most common character in the string. If there are multiple characters that appear the same number of times, return the character with the lowest ASCII value.

Example:
Input: "hello"
Output: "l"

Explanation:
In the input string "hello", the characters 'l' appears the most frequently, a total of 2 times. Therefore, the output should be "l".

Solution:
```python
def most_common_character(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    most_common_char = None
    max_count = 0
    
    for char, count in char_count.items():
        if count > max_count or (count == max_count and ord(char) < ord(most_common_char)):
            most_common_char = char
            max_count = count
    
    return most_common_char

# Test the function
print(most_common_character("hello"))  # Output: "l"
print(most_common_character("abcdeedcba"))  # Output: "a"
```

This function takes a string as input, counts the occurrence of each character in the string, and returns the most common character (with the lowest ASCII value in case of a tie).