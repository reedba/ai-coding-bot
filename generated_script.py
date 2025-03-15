Problem: Reverse a String

Explanation: Create a function that takes a string as input and returns the string reversed.

Solution in Python:

```python
def reverseString(s):
    # Convert the string to a list of characters
    s_list = list(s)
    
    # Use two pointers to swap characters from both ends of the list
    left, right = 0, len(s_list) - 1
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    
    # Convert the list back to a string and return
    return ''.join(s_list)

# Test the function
input_str = "hello"
output_str = reverseString(input_str)
print(output_str)  # Output: "olleh"
```