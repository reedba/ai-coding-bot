Problem:
Given an array of integers, rotate the array to the right by k steps, where k is a non-negative integer.

Example:
Input: [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
In the above example, the array is rotated to the right by 3 steps. The final output is [5,6,7,1,2,3,4].

Solution in Python:
```python
def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # normalize k if it is larger than the length of the array
    
    # Reverse the entire array
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)
    
    return nums

# Test the solution with the example input
nums = [1,2,3,4,5,6,7]
k = 3
result = rotate_array(nums, k)
print(result)
```

Output:
[5,6,7,1,2,3,4]