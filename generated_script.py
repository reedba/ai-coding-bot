Sure, I can help with that! Here's a new DSA problem for you to work on:

Problem: Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:
Input: nums = [1, 1, 2, 2, 3]
Output: 3 (since the input array is modified to [1, 2, 3])

Explanation:
To solve this problem, we can use two pointers, one to iterate through the array and another to keep track of the index where the next unique element should be placed. We will compare the current element with the next element in the array. If they are the same, we will skip over the duplicate element. If they are different, we will move the unique element to the next available index.

Here's a Python solution to the problem:

```python
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    
    unique_index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]
    
    return unique_index + 1

# Example usage
nums = [1, 1, 2, 2, 3]
print(removeDuplicates(nums))  # Output: 3
print(nums)  # Modified array: [1, 2, 3]
```

You can try implementing this solution and test it with different input arrays to see how it performs. Let me know if you have any questions or need further explanation!