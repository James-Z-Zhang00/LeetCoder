# 392. Is Subsequence

`https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75`

A two pointers problem that can be solved by O(n)

## Intuition

Instead of re-arranging the strings, we can simply use 2 pointers to check if letters we need appear in the certain order

Use 2 pointers like an asynchronous comparison method, return if they are match at the end

## Approach

We use a for-loop to get through every single character of the list t (the longer one) and use the element as one of our pointers

Inside the for-loop, check if `s[counter] == c` and make sure `counter < len(s)` , `if counter < len(s) and s[counter] == c:`.

Increment `counter` and `return counter == len(s)`

Don't forget to include 2 extreme situation at the beginning:
  1. len(s) > len(t)
  2. s is an empty string

## Code

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        '''
        Two Pointers
        '''

        if len(s) > len(t): return False
        if s is '': return True

        counter = 0

        for c in t:
            if counter < len(s) and s[counter] == c:
                counter += 1
        return counter == len(s)
```

## Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)