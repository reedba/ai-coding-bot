Problem: Given a string, return the most common character in the string.

Explanation:
To solve this problem, we can iterate through each character in the given string and keep track of the frequency of each character using a dictionary. Once we have found the frequency of each character, we can then find the character with the highest frequency.

Solution in Python:

```python
def most_common_char(s):
    char_freq = {}
    
    # Count the frequency of each character
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # Find the character with the highest frequency
    max_freq = 0
    most_common_char = ''
    for char, freq in char_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_common_char = char
    
    return most_common_char

# Test the function
s = "hello world"
print(most_common_char(s))  # Output: 'l'
```

This solution iterates through each character in the input string and counts the frequency of each character using a dictionary. Then, it finds the character with the highest frequency and returns it.