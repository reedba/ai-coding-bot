Problem: 

Given an array of integers, rotate the array to the right by k steps, where k is a non-negative integer.

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
After rotating the array to the right by 3 steps, the array becomes [5,6,7,1,2,3,4].

Solution in Python:

```python
def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # handling the case where k is greater than the length of the array
    
    nums[:] = nums[-k:] + nums[:-k]  # concatenate the two parts of the array after rotation
    
    return nums

# Example
nums = [1,2,3,4,5,6,7]
k = 3
result = rotate_array(nums, k)
print(result)  # Output: [5,6,7,1,2,3,4]
```

In this solution, we first calculate the effective rotation value (k % n) to handle cases where k is greater than the length of the array. Then, we concatenate the two parts of the array after rotation to get the final rotated array.