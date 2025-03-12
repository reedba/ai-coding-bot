Problem: 

Given an array of integers, return the indices of two numbers such that they add up to a specific target.

Example: 

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Solution:

```python
def two_sum(nums, target):
    hash_map = {} # create a hash map to store the numbers and their indices
    
    for i in range(len(nums)):
        complement = target - nums[i] # calculate the value that would sum up to the target
        
        if complement in hash_map: # if the complement is in the hash map, return the indices
            return [hash_map[complement], i]
        
        hash_map[nums[i]] = i # add the current number and its index to the hash map
    
    return None # if no pair sums up to the target, return None

# Test the function
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target)) # Output: [0, 1]
```

Explanation:

This solution uses a hash map to store the numbers and their indices as we iterate through the input array. For each number, we calculate the complement needed to reach the target sum. If the complement is already in the hash map, we return the indices of the two numbers. If no pair sums up to the target, we return None.