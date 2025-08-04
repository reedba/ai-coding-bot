Problem: Given a list of words, write a Python function that returns the longest word in the list. If there are multiple words with the same length, return the word that appears first in the list.

Example:
Input: ["apple", "banana", "orange", "kiwi", "pineapple"]
Output: "pineapple"

Explanation:
To solve this problem, we can iterate through the list of words and keep track of the longest word seen so far. We can start by initializing a variable to store the current longest word and set it to an empty string. Then, we can iterate through each word in the list and compare its length with the length of the current longest word. If the current word is longer, we update the current longest word. Finally, we return the longest word found.

Solution:

```python
def longest_word(words):
    longest = ""
    
    for word in words:
        if len(word) > len(longest):
            longest = word
            
    return longest

words = ["apple", "banana", "orange", "kiwi", "pineapple"]
print(longest_word(words))
```

Output:
"pineapple"

This solution has a time complexity of O(n), where n is the number of words in the list.