Problem: Given a string, return the first non-repeating character in it. If there are no non-repeating characters, return -1.

Example:
Input: "leetcode"
Output: "l"

Explanation:
In the input string "leetcode", the first non-repeating character is 'l'.

Solution in Python:
```python
def firstUniqChar(s: str) -> str:
    # Create a dictionary to store the frequency of each character in the string
    freq = {}
    
    # Count the frequency of each character
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    # Find the first non-repeating character in the string
    for char in s:
        if freq[char] == 1:
            return char
    
    return -1

# Test the function with the given example
input_str = "leetcode"
print(firstUniqChar(input_str))  # Output: "l"
```

In this solution, we first count the frequency of each character in the input string using a dictionary. Then, we iterate through the string again to find the first non-repeating character by checking if its frequency is 1. If we find such a character, we return it. If no non-repeating character is found, we return -1.