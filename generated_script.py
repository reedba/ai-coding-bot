Problem:

Given two strings, s1 and s2, write a function to determine if s2 is a rotation of s1.

Example:
s1 = "waterbottle"
s2 = "erbottlewat"

Explanation:
s2 is a rotation of s1 if we can split s1 into two parts, x and y, such that s1 = xy and s2 = yx. In the example above, s1 can be split into "water" and "bottle", and s2 can be rearranged to "bottle" and "water". Thus, s2 is a rotation of s1.

Solution:

```python
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in s1 + s1

s1 = "waterbottle"
s2 = "erbottlewat"
print(is_rotation(s1, s2))  # Output: True

s1 = "hello"
s2 = "world"
print(is_rotation(s1, s2))  # Output: False
```

Explanation:
The function `is_rotation` first checks if the lengths of both strings are equal, as a rotation can only occur if they are of the same length. It then checks if s2 is a substring of s1 concatenated with itself. If so, it returns True, indicating that s2 is a rotation of s1. Otherwise, it returns False.