Problem: Reverse a String

Explanation: Write a Python program to reverse a given string. For example, if the input string is "hello", the output should be "olleh".

Solution:

```python
def reverse_string(input_str):
    # Convert the input string to a list of characters
    str_list = list(input_str)
    
    # Initialize two pointers to the start and end of the list
    left = 0
    right = len(str_list) - 1
    
    # Swap characters from the beginning and end of the list
    while left < right:
        str_list[left], str_list[right] = str_list[right], str_list[left]
        left += 1
        right -= 1
    
    # Convert the list back to a string
    reversed_str = ''.join(str_list)
    
    return reversed_str

# Test the function with an example
input_str = "hello"
output_str = reverse_string(input_str)
print(output_str)  # Output: olleh
```

In this solution, we first convert the input string to a list of characters. We then use two pointers (one pointing to the start of the list and the other pointing to the end) to swap characters until we reach the middle of the list. Finally, we convert the list back to a string and return the reversed string.