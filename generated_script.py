Problem: Given a string, return the length of the longest palindrome that can be formed using the characters in the string.

Example:
Input: "abccccdd"
Output: 7
Explanation: One longest palindrome that can be formed is "dccaccd".

Solution:

```python
def longest_palindrome(s):
    char_count = {}  # Dictionary to store count of characters
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    palindrome_length = 0
    odd_count = 0  # Counter for characters with odd count
    
    for count in char_count.values():
        if count % 2 == 0:  # If count is even, all characters can be used in palindrome
            palindrome_length += count
        else:
            palindrome_length += count - 1  # If count is odd, one character can be used in palindrome
            odd_count += 1  # Increment odd count
    
    if odd_count > 0:
        palindrome_length += 1  # Add one odd count character as center of the palindrome
    
    return palindrome_length

# Test the function
input_str = "abccccdd"
print(longest_palindrome(input_str))  # Output: 7
```

Explanation:
- We first count the frequency of each character in the input string using a dictionary.
- We iterate through the counts of each character and add the count to the palindrome length. If the count is odd, we subtract 1 from the count and increment the odd count.
- Finally, we add one to the palindrome length for the odd count character to be used as the center of the palindrome.
- The final palindrome length is returned as the output.