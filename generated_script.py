Problem: Given an array of strings, write a function that returns the average length of all strings in the array. 

Explanation: We need to calculate the average length of all strings in the given array. To solve this problem, we can iterate through the array and calculate the total length of all strings. Then, we divide this total length by the number of strings in the array to get the average length.

Solution in Python:

```python
def average_length_of_strings(str_array):
    total_length = 0
    num_strings = len(str_array)
    
    # Calculate total length of all strings
    for string in str_array:
        total_length += len(string)
    
    # Calculate average length
    average_length = total_length / num_strings
    
    return average_length

# Test the function
strings = ["hello", "world", "python"]
result = average_length_of_strings(strings)
print(result)  # Output: 5.0
```

In this solution, we first initialize variables `total_length` and `num_strings` to keep track of the total length of all strings and the number of strings in the array respectively. We then calculate the total length by iterating through each string in the array and adding its length to the `total_length` variable. Finally, we calculate the average length by dividing the `total_length` by the `num_strings` and return the result.