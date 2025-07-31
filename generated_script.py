Problem:
Given a string, return the most common character in the string. If there are multiple characters that are equally common, return the character that appears first in the input string. 

Example:
Input: "abracadabra"
Output: "a"

Explanation:
In the input string "abracadabra", the character "a" appears 5 times, which is more than any other character in the string. Therefore, the output is "a".

Solution in Python:

```python
def most_common_char(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    max_count = 0
    most_common_char = None
    for char, count in char_count.items():
        if count > max_count:
            max_count = count
            most_common_char = char
    
    return most_common_char

# Test the function
input_string = "abracadabra"
print(most_common_char(input_string))  # Output: "a"
```

In the above solution, we first create a dictionary `char_count` to store the count of each character in the input string. We then loop through the input string to populate this dictionary. Finally, we iterate through the dictionary to find the character with the highest count and return it as the most common character in the string.