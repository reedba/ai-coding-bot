Problem: Reverse a String

Explanation: Write a function that takes a string as input and returns the string reversed.

Solution in Python:

```python
def reverse_string(s):
    return s[::-1]

# Test the function
input_str = "hello"
print(reverse_string(input_str))  # Output: "olleh"
```

In this solution, we are utilizing Python's slicing feature to reverse the input string. `s[::-1]` returns a new string with elements in reverse order.