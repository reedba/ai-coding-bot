Problem:

Given an array of integers, write a function to check if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example:
Input: [1, 2, 3, 1]
Output: true

Input: [1, 2, 3, 4]
Output: false

Explanation:
To solve this problem, we can create a set to store the elements we have seen so far while iterating through the array. If we encounter an element that is already in the set, we return true. If we reach the end of the array without finding any duplicates, we return false.

Solution in Python:

```python
def containsDuplicate(nums):
    num_set = set()
    
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    
    return False

# Test cases
print(containsDuplicate([1, 2, 3, 1])) # Output: true
print(containsDuplicate([1, 2, 3, 4])) # Output: false
```

This function has a time complexity of O(n) where n is the number of elements in the input array. The space complexity is also O(n) due to the set we are using to store the elements.