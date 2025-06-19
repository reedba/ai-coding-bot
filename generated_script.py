Problem: 

Given an array of integers, return a new array where each element is the product of all the elements in the original array except the element at that index.

Example:
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Explanation:
- For index 0, the product of all the elements except 1 is 2 * 3 * 4 = 24
- For index 1, the product of all the elements except 2 is 1 * 3 * 4 = 12
- For index 2, the product of all the elements except 3 is 1 * 2 * 4 = 8
- For index 3, the product of all the elements except 4 is 1 * 2 * 3 = 6

Solution in Python:
```python
def product_except_self(nums):
    n = len(nums)
    output = [1] * n
    
    # Calculate the product of all elements to the left of current index
    left_product = 1
    for i in range(n):
        output[i] *= left_product
        left_product *= nums[i]
    
    # Calculate the product of all elements to the right of current index
    right_product = 1
    for i in range(n-1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    
    return output

# Test the function
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]
```

In this solution, we first initialize a new array `output` with all elements as 1. We then calculate the product of all elements to the left of the current index and store it in the `output` array. Next, we calculate the product of all elements to the right of the current index and multiply it with the value already present in the `output` array. Finally, we return the `output` array.