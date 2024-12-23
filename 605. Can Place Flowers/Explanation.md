# 605. Can Place Flowers

Question link: `https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75`

## Intuition

This's a typical array processing question with time & space complexity `O(n)`, there are some conditions needed to take care:
1. Check if the first and the last element of the `flowerbed` is empty or not
2. After a valid position found, the number of that position should be change from 0 to 1 to avoid miscounting, so the system knows that the position is taken, won't consider it is empty
3. Don't forget to check if the element itself is 0, not only check its previous and the next elements
4. `n` could be 0, no flower needed to be placed on the `flowerbed`
5. After applying decrement to `n` keep that in mind `n` can go below 0 (negative value)

## Approach

Use a for-loop to check the element except the first and the last one, for each element, if its previous and its next element are 0 **and itself is 0**, this position is available, deduct `n`

```python
for i in range(1, len(flowerbed)-1):
    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
        flowerbed[i] = 1 
        n -= 1
```

Check the first and the last element first

```python
if flowerbed[0] == 0 and flowerbed[1] == 0:
    n -= 1
    flowerbed[0] = 1

if flowerbed[-1] == 0 and flowerbed[-2] == 0:
    n -= 1
    flowerbed[-1] = 1
```

Include the situation that the flowerbed could only have one place

```python
if len(flowerbed) == 1:
    if flowerbed[0] == 0: n-= 1
```

## Complexity

Time complexity is `O(n)` since it need to loop through the array

Space complexity is `O(n)` because it need to hold the data for the flowerbed

## The Code

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        Array

        Iterate
        '''

        if len(flowerbed) == 1:
            if flowerbed[0] == 0: n-= 1
        else:

            if flowerbed[0] == 0 and flowerbed[1] == 0:
                n -= 1
                flowerbed[0] = 1
    
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                n -= 1
                flowerbed[-1] = 1
    
            for i in range(1, len(flowerbed)-1):
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1 
                    n -= 1
    
        return n <= 0

```