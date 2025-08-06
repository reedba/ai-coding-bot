Problem: 
Given a string, return the most common character in the string. If there are multiple characters with the same maximum frequency, return all of them in a list.

Example:
Input: "abbcccdddeee"
Output: ['c', 'd', 'e']

Explanation:
In the input string "abbcccdddeee", the most common characters are 'c', 'd', and 'e' with a frequency of 3.

Solution in Python:

```python
def most_common_character(s):
    char_freq = {}
    
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    max_freq = max(char_freq.values())
    
    most_common_chars = [char for char, freq in char_freq.items() if freq == max_freq]
    
    return most_common_chars

# Test the function with the example
input_str = "abbcccdddeee"
output = most_common_character(input_str)
print(output)
```

Output:
['c', 'd', 'e']