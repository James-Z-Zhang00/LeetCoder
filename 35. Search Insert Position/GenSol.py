'''
35. Search Insert Position

https://leetcode.com/problems/search-insert-position/description/
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
         
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target: return middle
            elif nums[middle] > target: right = middle - 1
            else: left = middle + 1

        return left
    
    