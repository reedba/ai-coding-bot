Alright, here is a DSA problem related to strings and arrays:

Problem: Given an array of integers, return the indices of two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: The sum of 2 and 7 is 9, so the indices of the two numbers are 0 and 1.

Solution (Python):
```python
def twoSum(nums, target):
    num_dict = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_dict:
            return [num_dict[complement], i]
        else:
            num_dict[nums[i]] = i

# Input
nums = [2, 7, 11, 15]
target = 9

# Output
result = twoSum(nums, target)
print(result)
```

In this solution, we use a dictionary to store the numbers we have encountered so far. For each number in the array, we calculate its complement (target - current number) and check if the complement is already in the dictionary. If it is, we return the indices of the two numbers that add up to the target. If not, we add the current number to the dictionary.