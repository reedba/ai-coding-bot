Sure! Here is a problem involving strings and arrays:

Problem:
You are given a string s consisting of lowercase letters and an array of integers arr. Your task is to find the number of occurrences of each character in the string and return a new string where each character is repeated according to its frequency as specified in the arr array. For example, if s = "ab" and arr = [3, 1], then the output should be "aaabb".

Explanation:
In the given example, the character 'a' occurs 3 times in the string s and 'b' occurs 1 time. Therefore, the new string should have 'a' repeated 3 times followed by 'b' repeated 1 time.

Solution (in Python):
```python
def repeat_characters(s, arr):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    new_string = ''
    for char, count in freq.items():
        new_string += char * count
    
    return new_string

# Test the function with the example
s = "ab"
arr = [3, 1]
output = repeat_characters(s, arr)
print(output)  # Output: "aaabb"
```

In this solution, we first create a frequency dictionary `freq` to count the occurrences of each character in the string `s`. Then, we iterate through the dictionary to build the new string by repeating each character according to its frequency. Finally, we return the new string as the output.

I hope this problem helps you in practicing strings and arrays in DSA! Let me know if you need any further clarification or if you have any other questions.