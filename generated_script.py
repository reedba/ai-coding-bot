Problem: Given a string, return the first non-repeating character in the string. If there are no non-repeating characters, return -1.

Example:
Input: "leetcode"
Output: "l"

Explanation:
In the given input string, the character 'l' is the first non-repeating character (appears only once) in the string.

Solution in Python:

```python
def firstNonRepeatingChar(s):
    count = {}
    
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
            
    for char in s:
        if count[char] == 1:
            return char
    
    return -1

# Test the function
input_string = "leetcode"
output = firstNonRepeatingChar(input_string)
print(output)  # Output: "l"
```

In this solution, we first create a dictionary `count` to store the frequency of each character in the input string. Then, we iterate through the input string to update the frequency count. Finally, we iterate through the string again and return the first character with frequency of 1. If no such character exists, we return -1.