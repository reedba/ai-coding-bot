Problem: Given an array of integers, find the maximum sum of subarray within the array.

Explanation: To solve this problem, we can use the Kadane's algorithm. The algorithm involves iterating through the array and keeping track of the maximum sum of subarray ending at each element. We update the maximum sum by taking the maximum of the current element and the sum of the element with the maximum sum ending at the previous element.

Solution in Python:

```python
def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test the function
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  # Output should be 6 (sum of [4, -1, 2, 1])
```

In this solution, we iterate through the array and update the current sum and maximum sum accordingly. The `max_subarray_sum` function returns the final maximum sum of the subarray.