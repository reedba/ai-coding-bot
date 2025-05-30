Problem: 

Given a string, return the most common character in the string. If there are multiple characters with the same highest frequency, return all of them.

Example:
Input: "hello"
Output: ['l']

Explanation:
In the input string "hello", the most common character is 'l', which appears twice. Therefore, the output is ['l'].

Solution in Python:

```python
from collections import Counter

def most_common_character(s):
    freq = Counter(s)
    max_freq = max(freq.values())
    result = [char for char, count in freq.items() if count == max_freq]
    return result

# Test the function with the example input
input_str = "hello"
output = most_common_character(input_str)
print(output)
```

This code uses the Counter class from the collections module to quickly find the frequency of each character in the input string. Then, it finds the maximum frequency and returns all characters that have that frequency. The result is then printed.