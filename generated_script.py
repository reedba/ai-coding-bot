Problem:
Given an array of integers, write a function that returns the maximum product of any three numbers in the array.

Example:
Input: [3, 5, 2, 6, 4]
Output: 120 (5 * 6 * 4)

Explanation:
To find the maximum product of three numbers in the array, we need to consider all possible combinations of three numbers. We can achieve this by sorting the array and then multiplying the maximum three numbers, or by finding the maximum and minimum numbers in the array and considering the product of those numbers with the maximum number.

Solution in Python:

```python
def max_product_of_three(nums):
    nums.sort()
    n = len(nums)
    return max(nums[0]*nums[1]*nums[n-1], nums[n-1]*nums[n-2]*nums[n-3])

# Example
nums = [3, 5, 2, 6, 4]
print(max_product_of_three(nums))  # Output: 120
```

This solution sorts the array in ascending order and then calculates the maximum product in two ways: by multiplying the minimum two numbers with the maximum number, or by multiplying the three maximum numbers in the array. Finally, it returns the maximum of these two products as the result.