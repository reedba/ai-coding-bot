Problem:
Write a Python function that takes in a string and returns the most common character in the string. If there are multiple characters with the same highest frequency, return the character that appears first in the string.

Example:
Input: "programming"
Output: "m"

Explanation:
In the given input string "programming", the character "m" appears 2 times, which is the highest frequency compared to other characters in the string.

Solution:

```python
def most_common_char(string):
    char_freq = {}
    max_freq = 0
    most_common_char = ''
    
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
        
        if char_freq[char] > max_freq:
            max_freq = char_freq[char]
            most_common_char = char
    
    return most_common_char

# Test the function with example
input_string = "programming"
print(most_common_char(input_string))  # Output: "m"
```

This function first initializes an empty dictionary `char_freq` to keep track of the frequency of each character in the input string. It then iterates through each character in the string, updating the frequency count in the dictionary. The function also keeps track of the character with the highest frequency encountered so far, updating it if a character with a higher frequency is found. Finally, the function returns the most common character based on the frequency count.