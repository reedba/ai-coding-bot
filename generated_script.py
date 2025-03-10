Problem: Given a string, s, find the length of the longest substring without repeating characters.

Explanation:
We can solve this problem by using a sliding window approach. We will iterate through the string using two pointers, start and end, to keep track of the current substring. We will also maintain a set to store the characters we have seen so far.

As we iterate through the string, if the character at the end pointer is already in the set, we will remove the character at the start pointer from the set and increment the start pointer until the set does not contain the current character. This will help us find the longest substring without repeating characters.

Solution:

```python
def length_of_longest_substring(s: str) -> int:
    n = len(s)
    start = 0
    end = 0
    max_length = 0
    seen = set()
    
    while end < n:
        if s[end] not in seen:
            seen.add(s[end])
            end += 1
            max_length = max(max_length, end - start)
        else:
            seen.remove(s[start])
            start += 1
    
    return max_length

# Test the function
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3
```

In this solution, we iterate through the string 's' and use a set 'seen' to keep track of the characters we have seen so far. The 'start' and 'end' pointers are used to maintain the current substring. The maximum length of the substring without repeating characters is updated at each step. Finally, we return the maximum length of the substring.

You can test this solution with different input strings to verify its correctness.