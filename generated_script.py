Problem: 
Given a string, return the most common character in the string. If there are multiple characters that are equally common, return the first character that appears in the string.

Explanation:
To solve this problem, we will iterate through each character in the string and keep track of the frequency of each character using a dictionary. Once we have the frequencies of all characters, we will find the character with the highest frequency and return it.

Solution:
```python
def most_common_char(s):
    freq = {}
    
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    max_freq = 0
    most_common_char = ''
    
    for char, count in freq.items():
        if count > max_freq:
            max_freq = count
            most_common_char = char
    
    return most_common_char

# Test the function
s = "hello world"
print(most_common_char(s))  # Output: 'l'
```

In this solution, we iterate through each character in the input string 's' and update the frequency of each character in the 'freq' dictionary. We then find the character with the highest frequency and return it as the most common character in the string.