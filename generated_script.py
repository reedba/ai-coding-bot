Problem: Given a string, return the most common character in the string. If there are multiple characters that occur with the same frequency, return the one that comes first in the string.

Example:
Input: "hello"
Output: "l"

Explanation:
In the input string "hello", the character 'l' occurs 2 times, which is more than any other character in the string.

Solution:
```
def most_common_char(input_string):
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    max_count = 0
    most_common_char = ''
    
    for char, count in char_count.items():
        if count > max_count:
            max_count = count
            most_common_char = char
    
    return most_common_char

# Test the function
input_string = "hello"
print(most_common_char(input_string))  # Output: "l"
```

In this solution, we first iterate through the input string and count the occurrences of each character in a dictionary. Then, we iterate through the dictionary to find the character with the highest count, which is the most common character in the string. Finally, we return the most common character.