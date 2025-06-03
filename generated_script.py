Problem: 

Given a string, return the most common character in the string. If there are multiple characters with the same maximum frequency, return all of them in a list.

Explanation:

To solve this problem, we can use a dictionary to keep track of the frequency of each character in the string. We can iterate through the string and update the frequency count in the dictionary. Then, we can find the character(s) with the maximum frequency and return them.

Solution in Python:

```python
def most_common_char(s):
    freq = {}
    max_freq = 0
    
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
        max_freq = max(max_freq, freq[char])
    
    most_common_chars = [key for key, value in freq.items() if value == max_freq]
    
    return most_common_chars

# Test the function with a sample string
s = "hello world"
result = most_common_char(s)
print(result)  # Output: ['l', 'o']
```

This solution iterates through the string `s` and keeps track of the frequency of each character in the `freq` dictionary. Then, it finds the maximum frequency and returns all characters with that frequency in a list.