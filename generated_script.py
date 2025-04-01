Problem:
Given a string, write a function to reverse the string in-place.

Explanation:
In this problem, we are given a string and we need to reverse the string in-place, meaning we cannot use any extra space to store the reversed string. We have to modify the given string itself to achieve the desired result.

Solution:

```python
def reverse_string(s):
    # Convert the string to a list of characters for in-place manipulation
    s = list(s)
    
    # Two pointers approach to reverse the string
    left = 0
    right = len(s) - 1
    while left < right:
        # Swap characters at left and right pointers
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        
    # Convert the list of characters back to a string
    return "".join(s)

# Test the function with an example
s = "hello"
print(reverse_string(s))  # Output: "olleh"
```

In this solution, we first convert the input string `s` into a list of characters to perform in-place manipulation. We then use a two-pointers approach to swap characters from the beginning and end of the string until we reach the middle of the string. Finally, we convert the list of characters back to a string and return the reversed string.