Problem:
Given a string, write a function to find the longest substring without repeating characters.

Explanation:
For example, the input "abcabcbb" should return "abc" as the longest substring without repeating characters.

Solution:

```python
def longest_substring(input_str):
    # Initialize variables
    start = 0  # Start index of the current substring
    max_len = 0  # Length of the longest substring
    char_index = {}  # Dictionary to store index of characters
    
    # Loop through the input string
    for i in range(len(input_str)):
        char = input_str[i]
        
        # Check if the character is already in the char_index dictionary
        if char in char_index and char_index[char] >= start:
            # Update the start index to the next index of the repeated character
            start = char_index[char] + 1
        
        # Update the index of the character in the char_index dictionary
        char_index[char] = i
        
        # Update the max_len if the current substring is longer
        max_len = max(max_len, i - start + 1)
    
    # Return the longest substring without repeating characters
    return input_str[start:start + max_len]

# Test the function
input_str = "abcabcbb"
print(longest_substring(input_str))  # Output: "abc"
```

In this solution, we use a sliding window approach to iterate through the input string while keeping track of the start index of the current substring, the length of the longest substring, and the index of each character. We update these variables as we encounter repeating characters to find the longest substring without repeating characters.