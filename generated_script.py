Problem:
Given a string, reverse the order of characters in each word while maintaining the order of words in the sentence.

Example:
Input: "hello world"
Output: "olleh dlrow"

Explanation:
In the input string, the word "hello" is reversed to "olleh" and the word "world" is reversed to "dlrow". The order of words remains the same, with "hello" coming before "world".

Solution in Python:
```python
def reverseWords(s):
    # Split the input string into individual words
    words = s.split()
    
    # Iterate through each word and reverse the characters
    for i in range(len(words)):
        words[i] = words[i][::-1]
    
    # Join the reversed words back together to form the final output
    return ' '.join(words)

# Test the function with an example input
input_str = "hello world"
output_str = reverseWords(input_str)
print(output_str)  # Output: "olleh dlrow"
```

In this solution, we first split the input string `s` into individual words using the `split()` function. We then iterate through each word and reverse its characters using the slicing syntax `[::-1]`. Finally, we join the reversed words back together using the `join()` function and return the final output.