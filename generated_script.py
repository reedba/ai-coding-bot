Problem: Given a string, write a function that returns the most common character in the string.

Explanation:
To solve this problem, we can iterate through each character in the string and keep track of the frequency of each character in a dictionary. We can then find the character with the highest frequency and return it.

Solution in Python:

```python
def most_common_character(s):
    # Create a dictionary to store the frequency of each character
    char_count = {}
    
    # Iterate through each character in the string and update the frequency
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the character with the highest frequency
    max_char = max(char_count, key=char_count.get)
    
    return max_char

# Test the function
s = "hello world"
print(most_common_character(s))  # Output: 'l'
```

In this solution, we first initialize an empty dictionary `char_count` to store the frequency of each character. We then iterate through each character in the string `s` and update the frequency in the dictionary. Finally, we find the character with the highest frequency using the `max` function and return it.

This function has a time complexity of O(n) where n is the length of the input string since we iterate through the string only once.