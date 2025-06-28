Problem: 
Given an array of integers, find the maximum absolute difference between any two elements in the array.

Input:
- An array of integers

Output:
- An integer representing the maximum absolute difference between any two elements in the array

Example:
Input: [2, 4, 1, 7, 5]
Output: 6
Explanation: The maximum absolute difference can be found between the elements 1 and 7 (|7 - 1| = 6)

Solution (in Python):
```python
def max_absolute_difference(arr):
    if len(arr) < 2:
        return 0
    
    min_val = arr[0]
    max_val = arr[0]
    
    for num in arr:
        min_val = min(min_val, num)
        max_val = max(max_val, num)
    
    return abs(max_val - min_val)

# Test the function with the example input
arr = [2, 4, 1, 7, 5]
print(max_absolute_difference(arr))
```

This solution has a time complexity of O(n) where 'n' is the number of elements in the input array.