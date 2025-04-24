Problem: Given a string, reverse all the words within the string.

Example:
Input: "Hello World"
Output: "olleH dlroW"

Explanation:
To solve this problem, we can first split the input string into individual words, then reverse each word separately, and finally join the reversed words back together to form the final output string.

Solution in Python:

```python
def reverse_words(input_str):
    # Split the input string into individual words
    words = input_str.split()
    
    # Reverse each word in the list
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words back together to form the final output string
    output_str = " ".join(reversed_words)
    
    return output_str

# Test the function with the example input
input_str = "Hello World"
output = reverse_words(input_str)
print(output)  # Output: "olleH dlroW"
```

This solution first splits the input string into individual words using the `split()` method, then reverses each word using list comprehension and the slicing technique `[::-1]`, and finally joins the reversed words back together to form the final output string.