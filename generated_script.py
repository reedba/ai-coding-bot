Problem: Given a string, write a function to reverse the string in-place. Do not use any extra space for another array. 

Example:
Input: "hello"
Output: "olleh"

Explanation: In-place reversal means that the input string should be modified directly. So, you should not create a new string or use any additional data structure to solve this problem. 

Solution in Python:

```python
def reverse_string(s):
    # Convert the string to a list to make it mutable
    s = list(s)
    
    # Initialize two pointers, one at the beginning and one at the end
    left, right = 0, len(s) - 1
    
    while left < right:
        # Swap characters at the two pointers
        s[left], s[right] = s[right], s[left]
        
        # Move the pointers towards the center
        left += 1
        right -= 1
        
    # Convert the list back to string
    return ''.join(s)

# Test the function with an example
input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)  # Output: "olleh"
```

This solution uses two pointers to swap characters at the beginning and end of the string until they reach the middle. This approach reverses the string in-place without using any extra space.