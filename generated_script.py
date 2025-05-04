Problem:

Given a string and a target character, write a function to return the index of the first occurrence of the target character in the string. If the target character is not found in the string, return -1.

Example:
Input: str = "hello", target = "e"
Output: 1

Input: str = "hello", target = "a"
Output: -1

Explanation:
In the first example, the target character "e" is found at index 1 in the string "hello".
In the second example, the target character "a" is not found in the string "hello", so the output is -1.

Solution in Python:

```python
def first_occurrence_index(s, target):
    for i in range(len(s)):
        if s[i] == target:
            return i
    return -1

# Test cases
str1 = "hello"
target1 = "e"
print(first_occurrence_index(str1, target1)) # Output: 1

str2 = "hello"
target2 = "a"
print(first_occurrence_index(str2, target2)) # Output: -1
```

This function iterates through each character in the given string and checks if it matches the target character. If a match is found, it returns the index of that character. If no match is found, it returns -1.