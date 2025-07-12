Problem:

Given a string, create a function to reverse the string in-place without using any extra space.

Explanation:

In this problem, we are asked to reverse a given string in-place, meaning we cannot create a new string and must modify the original string. We can achieve this by using two pointers, one starting at the beginning of the string and one at the end of the string, and swapping the characters at these positions until we reach the middle of the string.

Solution in Python:

```python
def reverse_string_in_place(s):
    # Convert the string to a list so that we can modify it in place
    s = list(s)
    
    # Initialize two pointers, one at the beginning and one at the end of the string
    start = 0
    end = len(s) - 1
    
    while start < end:
        # Swap the characters at the start and end pointers
        s[start], s[end] = s[end], s[start]
        # Move the pointers towards the middle of the string
        start += 1
        end -= 1
        
    # Convert the list back to a string
    return ''.join(s)

# Test the function
s = "hello"
print(reverse_string_in_place(s))  # Output: "olleh"
``` 

This function takes a string `s` as input, converts it to a list, and then reverses the characters in-place using two pointers. Finally, it converts the reversed list back to a string and returns it.