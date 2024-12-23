# 345. Reverse Vowels of a String

Question link `https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75`

2 ideas
- Double loop (brute force)
- Swapping (slightly better, 2 pointers)

## Intuition (Double Loop)

This's a typical array question, we are going to loop through the string, find the vowels and replace. Remember we are not able to modify a string in Python, we are creating a new string instead for our final answer/result

## Approach (Double Loop)

Use an empty list to save the `vowels` in order and a string `s2` as our answer

```python
vowels = []
s2 = ""
```

Find the `vowels` in their appeared orders, reverse the list to get the reverse vowel orders

```python
for c in s:
    if c in ['a','e','i','o','u','A','E','I','O','U']:
        vowels.append(c)
vowels.reverse()
```

Forming the answer string `s2` by looping through the original string again but replace the `vowels`

If the char is a vowel, append the char from an element in the reversed vowel list, otherwise append other letters as usual

```python
for i in range(len(s)):
    if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
        s2 += vowels[0]
            vowels = vowels[1:]
    else:
        s2 += s[i]
```

## Code (Double Loop)

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        s2 = ""
        for c in s:
            if c in ['a','e','i','o','u','A','E','I','O','U']:
                vowels.append(c)
        vowels.reverse()

        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                s2 += vowels[0]
                vowels = vowels[1:]
            else:
                s2 += s[i]
        return s2
```

## Complexity (Double Loop)

Time complexity `O(2n)` which is `O(n)`, we go through the list twice
Space complexity `O(2n)` which is `O(n)`, we need spaces for 2 strings the original and the answer

## Intuition (Swapping, 2 pointers)

Instead of going through the string twice, we can simply swap 2 vowels *the first and the last, the second and the second last and so on*, to do this, we need 2 pointers

Since strings are immutable in Python, we convert it into a list to do the modification, then convert it back to a string after we finish

## Approach (Swapping, 2 pointers)

Initialize the 2 pointers, convert list and the vowels checking, where `word` is the converted list for string `s` and the `end` pointer should be `len(s) - 1` due to one-off index counting

```python
word = list(s)
start = 0
end = len(s) - 1
vowels = "aeiouAEIOU"
```

A while loop for the 2 pointers, locate the first and the last vowel

```python
while start < end:
    while start < end and vowels.find(word[start]) == -1:
        start += 1
    while start < end and vowels.find(word[end]) == -1:
        end -= 1   
```

Swap the vowels and increment the pointers for the next search, 2 pointers should get closer to the middle

```python
word[start], word[end] = word[end], word[start]
start += 1
end -= 1
```

Convert the list `word` back to string as our final answer

```python
return "".join(word)
```

## Code (Swapping, 2 pointers)

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert the input string to a character array.
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"
        
        # Loop to get the start and the end pointer closer
        while start < end:
            # Locate the first vowel on the left hand side
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            
            # Locate the first vowel on the right hand side
            while start < end and vowels.find(word[end]) == -1:
                end -= 1
            
            # Swap the vowels
            word[start], word[end] = word[end], word[start]
            
            # Move the pointers towards each other for the next checking
            start += 1
            end -= 1
        
        # Convert the character array back to a string and return the result
        return "".join(word)
```

## Complexity (Swapping, 2 pointers)

Time complexity: `O(n)`, although 2 pointers checking from the beginning and the end, the worest case scenario would be 1 pointer through the whole string 

Space complexity: `O(n)`, we need some space to hold a list that has the same length as the string

*Although eventually both ideas got the same time and space complexity, the second idea (swapping) is a typical 2 pointers approach, this way of thinking could be extremely helpful in the future algorithm crackings*
