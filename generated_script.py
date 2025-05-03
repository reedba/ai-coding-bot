Problem: 
Given a string, write a Python function to reverse the characters in the string in-place.

Explanation:
The goal of this problem is to reverse a given string without using any additional space. We are to modify the original string directly.

Solution:

```python
def reverse_string(s):
    s = list(s) # convert string to list of characters
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left] # swap characters at left and right indices
        left += 1
        right -= 1
    return ''.join(s) # convert list back to string

# Testing the function
s = "hello"
print(reverse_string(s)) # Output: "olleh"
```

In this solution, we first convert the input string to a list of characters. We then use two pointers (left and right) to traverse the list from both ends and swap the characters at the left and right indices. Finally, we convert the list back to a string and return the reversed string.

This solution has a time complexity of O(n) and space complexity of O(1), as we are modifying the original string in-place without using any additional space.