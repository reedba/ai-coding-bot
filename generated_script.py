Problem: Given a string, implement a function to determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Explanation: To solve this problem, we can use two pointers approach. We can have one pointer start from the beginning of the string and another pointer start from the end of the string. As we compare the characters at these two pointers, if they are not the same, then the string is not a palindrome. If all characters match at their respective positions, then the string is a palindrome.

Solution:

```python
def is_palindrome(input_str):
    # Convert the string to lowercase and remove spaces
    input_str = input_str.lower().replace(" ", "")
    
    # Initialize two pointers
    left_ptr = 0
    right_ptr = len(input_str) - 1
    
    # Loop until pointers meet
    while left_ptr < right_ptr:
        # Skip non-alphanumeric characters
        if not input_str[left_ptr].isalnum():
            left_ptr += 1
        elif not input_str[right_ptr].isalnum():
            right_ptr -= 1
        # Compare characters at both pointers
        elif input_str[left_ptr] != input_str[right_ptr]:
            return False
        else:
            left_ptr += 1
            right_ptr -= 1
    
    return True

# Test the function with some examples
print(is_palindrome("A man a plan a canal Panama"))
# Output: True

print(is_palindrome("race a car"))
# Output: False
```

This function first converts the input string to lowercase and removes any spaces. It then initializes two pointers at the beginning and end of the string and iterates through the string, comparing characters at each position. If the characters do not match, it immediately returns False. If all characters match, it returns True. The function also skips non-alphanumeric characters while comparing.