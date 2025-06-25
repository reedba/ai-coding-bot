Problem: Given a string, implement a function to reverse the order of words in the string.

Explanation:

For example, given the input string "Hello World", the output should be "World Hello".

Solution in Python:
```python
def reverse_words(s):
    words = s.split() # Split the string into a list of words
    words.reverse() # Reverse the order of words
    return ' '.join(words) # Join the words back together with a space

# Test the function
input_string = "Hello World"
output_string = reverse_words(input_string)
print(output_string) # Output: "World Hello"
```

In this solution, we first split the input string into a list of words using the split() function. Then, we reverse the order of the words using the reverse() method. Finally, we join the words back together using the join() method with a space as the delimiter.