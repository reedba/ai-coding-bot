Problem:

Given a string, write a function to reverse the order of words in the string.

Explanation:

For example, given the input string "hello world", the output should be "world hello".

Solution in Python:

```python
def reverse_words(s):
    words = s.split()  # split the string by spaces to get individual words
    reversed_words = words[::-1]  # reverse the order of words
    reversed_string = ' '.join(reversed_words)  # join the reversed words back into a string
    return reversed_string

# Test the function
input_string = "hello world"
output_string = reverse_words(input_string)
print(output_string)  # Output: "world hello"
```

In this solution, we first split the input string into individual words using the `split()` method. We then reverse the order of the words using list slicing and join them back together using the `join()` method to form the final reversed string.