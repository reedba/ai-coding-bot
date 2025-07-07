Problem: Reverse a string

Explanation:
Write a function that takes in a string as input and returns the string reversed. For example, if the input is "hello", the output should be "olleh".

Solution in Python:
```python
def reverse_string(input_str):
    # Convert the string to a list to make it mutable
    input_list = list(input_str)
    
    # Initialize two pointers, one at the start and one at the end of the list
    left = 0
    right = len(input_list) - 1
    
    # Swap the characters at the two pointers and move the pointers towards each other until they meet in the middle
    while left < right:
        input_list[left], input_list[right] = input_list[right], input_list[left]
        left += 1
        right -= 1
    
    # Convert the list back to a string and return it
    return "".join(input_list)

# Test the function with an example
input_str = "hello"
output_str = reverse_string(input_str)
print(output_str)  # Output: "olleh"
```

This solution solves the problem by swapping characters at the two ends of the string and moving towards the middle until the whole string is reversed. The time complexity of this solution is O(n) where n is the length of the input string.