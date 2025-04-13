Problem: Given a string, write a function to determine if it is a palindrome (a word, phrase, number, or other sequence of characters that reads the same forward and backward).

Example:
Input: "racecar"
Output: True

Explanation: The string "racecar" is a palindrome because it reads the same forwards and backwards.

Solution in Python:

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "") # Convert the string to lowercase and remove spaces
    return s == s[::-1] # Check if the string is equal to its reverse

# Test the function
input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string)) # Output: True
``` 

In this solution, we first convert the input string to lowercase and remove any spaces using the `replace()` method. Then, we use slicing (`[::-1]`) to reverse the string and check if it is equal to the original string. If they are equal, the function returns `True`, indicating that the input is a palindrome.