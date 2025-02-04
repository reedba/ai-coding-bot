Problem: Write a function that takes in a string and returns the most common character in the string. If there are multiple characters with the same frequency, return the first character encountered.

Explanation:
To solve this problem, we can iterate through the string and store the frequency of each character in a dictionary. We then loop through the dictionary to find the character with the highest frequency.

Solution in Python:
```python
def most_common_character(s):
    char_frequency = {}
    
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    max_freq_char = ''
    max_freq = 0
    for char, freq in char_frequency.items():
        if freq > max_freq:
            max_freq = freq
            max_freq_char = char
            
    return max_freq_char

# Test the function
test_string = "hello"
print(most_common_character(test_string))  # Output: 'l'
```

In this solution, we first create an empty dictionary `char_frequency` to store the frequency of each character in the input string `s`. We then iterate through each character in `s` and update the frequency in the `char_frequency` dictionary.

Finally, we loop through the dictionary to find the character with the maximum frequency and return that character as the most common character.