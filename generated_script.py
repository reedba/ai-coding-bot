Problem:
Given a string, find the longest substring without repeating characters.

Example:
Input: "abcabcbb"
Output: 3 (The longest substring without repeating characters is "abc")

Explanation:
One way to solve this problem is by using a sliding window approach. We can keep track of the characters seen so far in a dictionary and update the start index of the window whenever we encounter a repeating character.

Solution (in Python):

```python
def longest_substring_without_repeating(s):
    char_dict = {}
    start = 0
    max_length = 0
    
    for end in range(len(s)):
        if s[end] in char_dict:
            start = max(start, char_dict[s[end]] + 1)
        char_dict[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Test the function
input_string = "abcabcbb"
print(longest_substring_without_repeating(input_string))  # Output: 3
```

In this solution, we maintain a dictionary `char_dict` to keep track of the last seen index of each character. We iterate over the input string with a sliding window defined by the `start` and `end` indices. Whenever we encounter a repeating character, we update the `start` index to the next index after the last occurrence of that character. We update the maximum length if necessary and return the final result.