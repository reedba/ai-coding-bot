Problem: 
You are given a string in the form of a sentence. Your task is to reverse the words in the sentence, but keep the words in the same order.

Input: 
A string representing a sentence. 

Output: 
A string with words in the reversed order.

Example:
Input: "Hello World"
Output: "olleH dlroW"

Explanation:
To solve this problem, we can first split the input string by space to get individual words. Then, we can reverse the order of the words and concatenate them back together.

Solution in Python:

```python
def reverse_words(sentence):
    words = sentence.split()  # split the sentence into individual words
    reversed_words = [word[::-1] for word in words]  # reverse each word in the list
    reversed_sentence = " ".join(reversed_words)  # join the reversed words back together
    return reversed_sentence

# Test the function with example
test_sentence = "Hello World"
result = reverse_words(test_sentence)
print(result)  # Output : "olleH dlroW"
```

By following this approach, we can reverse the words in a given sentence while maintaining the order of the words.