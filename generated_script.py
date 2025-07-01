Problem:
Given a string, return the most common character in the string. If there are multiple characters with the same highest frequency, return all of them.

Example:
Input: "hello world"
Output: ['l', 'o']

Explanation:
In the input string "hello world", the character 'l' and 'o' both occur 2 times, which is the highest frequency in the string. Therefore, we return ['l', 'o'].

Solution in Python:
```python
def most_common_chars(s):
    max_freq = 0
    char_freq = {}
    for char in s:
        if char.isalpha():
            char_lower = char.lower()
            char_freq[char_lower] = char_freq.get(char_lower, 0) + 1
            max_freq = max(max_freq, char_freq[char_lower])

    most_common_chars = [char for char, freq in char_freq.items() if freq == max_freq]
    return most_common_chars

# Test the function
input_str = "hello world"
print(most_common_chars(input_str))  # Output: ['l', 'o']
```

In this solution, we iterate through each character in the input string and keep track of the frequency of each character in a dictionary. We also keep track of the maximum frequency encountered. Finally, we filter out the characters with the maximum frequency and return them as a list.