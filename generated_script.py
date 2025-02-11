Problem: Given a string containing only lowercase letters, write a function to count the frequency of each letter in the string and return a dictionary with the letter as the key and its frequency as the value.

Example:
Input: "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

Explanation:
In the input string "hello", the letter 'h' appears once, 'e' appears once, 'l' appears twice, and 'o' appears once. The function should output a dictionary mapping each unique letter to its frequency.

Solution in Python:

```python
def count_letter_frequency(s):
    freq_dict = {}
    
    for letter in s:
        if letter in freq_dict:
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1
    
    return freq_dict

# Test the function
input_string = "hello"
print(count_letter_frequency(input_string))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

In the solution above, we iterate through each character in the input string, update the frequency count in the dictionary, and finally return the dictionary mapping each unique letter to its frequency.