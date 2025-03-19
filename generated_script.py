Problem: Given a string, write a Python function to reverse the string in-place.

Explanation: In this problem, we are asked to reverse a given string in-place, which means we cannot create a new string and must manipulate the original string itself.

Solution:
```python
def reverse_string(s):
    string_list = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        string_list[left], string_list[right] = string_list[right], string_list[left]
        left += 1
        right -= 1
    
    return ''.join(string_list)

# Test the function
s = 'hello'
print(reverse_string(s))  # Output: 'olleh'
```

In the solution, we first convert the input string `s` into a list of characters for easier manipulation. We then use two pointers, `left` and `right`, starting from the beginning and end of the string respectively, and swap the characters at these positions. We continue this process until `left` is no longer less than `right`, at which point we have successfully reversed the string in-place. Finally, we convert the list back to a string and return the reversed string.