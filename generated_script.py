Problem: Given a string, return a list of all unique characters in the string.

Explanation: We are given a string, and we need to find and return a list of all unique characters present in the string. For example, if the input string is "hello", the output should be ['h', 'e', 'l', 'o'].

Solution in Python:

```python
def unique_characters(string):
    unique_chars = []
    seen_chars = set() # to keep track of characters we have already seen
    
    for char in string:
        if char not in seen_chars:
            unique_chars.append(char)
            seen_chars.add(char)
    
    return unique_chars

# Test the function
input_string = "hello"
print(unique_characters(input_string)) # Output: ['h', 'e', 'l', 'o']
```

This solution iterates through each character in the input string and adds it to the `unique_chars` list only if it has not been seen before (i.e., not present in the `seen_chars` set). This ensures that each unique character is added only once to the final list.