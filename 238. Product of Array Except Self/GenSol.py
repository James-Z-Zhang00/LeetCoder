class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Array

        Brute Force: O(n^2)
        Algorithm: O(n)
        '''
        prefix_product = 1
        postfix_product = 1
        n = len(nums)
        res = [1] * n
        
        for i in range(n):
            res[i] *= prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            res[i] *= postfix_product
            postfix_product *= nums[i]
        return res