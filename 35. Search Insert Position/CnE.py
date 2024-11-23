'''
35. Search Insert Position

https://leetcode.com/problems/search-insert-position/description/
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = left + (right - left) // 2
            # left, right = (middle + 1, right) if nums[middle] < target else (left, middle)
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left
    
''' Where the LEFT in middle = LEFT + (right - left) // 2 makes sure that the whole searching window is moving steady towards right when searching for very large target values '''

''' Use tuple assignment to shorthand if statement '''