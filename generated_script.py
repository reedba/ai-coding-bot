Problem: Given a string, reverse the string in-place without using any additional data structures.

Explanation: In this problem, we are tasked with reversing a string in-place, meaning we need to modify the original string itself without using any additional data structures such as arrays or lists.

Solution in Python:
```python
def reverse_string(s):
    # convert string to a list of characters
    s = list(s)
    
    # two pointers approach to reverse the string in-place
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    # convert back to string and return
    return "".join(s)

# Example
input_str = "hello"
output_str = reverse_string(input_str)
print(output_str)  # Output: "olleh"
```

Explanation of the solution:
1. We first convert the input string `s` into a list of characters to make it easier to modify.
2. We then use a two-pointer approach where we have a `left` pointer starting from the beginning of the string and a `right` pointer starting from the end of the string.
3. We swap the characters at the `left` and `right` pointers and move the pointers towards each other until they meet in the middle, effectively reversing the string in-place.
4. Finally, we convert the list of characters back to a string using the `join` method and return the reversed string.

This solution has a time complexity of O(n) where n is the length of the input string, as we iterate through half of the string to reverse it.