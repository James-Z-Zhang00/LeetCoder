# 283. Move Zeroes

2 ideas:
  1. Find the number of 0s in the list, remove them all and append them at the end of the list, use `.extend([0]*count)` for Python instead of `.append(...)`
  2. Two pointers approach

## Approach (2 Pointers)

Create 2 pointers `fast` and `slow`, use a `for-loop` where fast pointer go through each element of the list

```python
slow = 0
for fast in range(len(nums)):
```

Always skip the first element

For the second element, swap it with the first element

```python
if nums[fast] != 0 and nums[slow] == 0:
    nums[slow], nums[fast] = nums[fast], nums[slow]
```