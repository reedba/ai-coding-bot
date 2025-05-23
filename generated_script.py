Problem: Given a string, write a function that returns the most common character in the string. If there are multiple characters with the same highest frequency, return the character that appears first in the string.

Example:
Input: "hello"
Output: 'l'

Explanation:
In the input string "hello", the character 'l' appears the most frequently with a frequency of 2.

Solution in Python:

```python
def most_common_char(s):
    char_count = {}
    max_count = 0
    most_common_char = ""
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        
        if char_count[char] > max_count:
            max_count = char_count[char]
            most_common_char = char
            
    return most_common_char

# Test the function with input "hello"
print(most_common_char("hello"))  # Output: 'l'
```

In this solution, we iterate through the input string and maintain a dictionary to keep track of the frequency of each character. We update the most common character and its frequency as we iterate through the input string. Finally, we return the most common character.