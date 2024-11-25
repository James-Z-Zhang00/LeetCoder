'''
27. Remove Element
https://leetcode.com/problems/remove-element/description/
2 Solutions
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [n for n in nums if n != val]
        # List slicing
        return len(nums)
        # Return the non-val amount

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Require to return the counter as well as to change the nums
        # that the first few elements must not equal to val
        # other sequence does not matter
        counter = 0
        for n in nums:
            # Loop through the list
            if n != val:
                # If the element is not val, set the element from the beginning of the list
                nums[counter] = n
                counter += 1
                # Update counter as index for the next set and amount tracking
        return counter
        # Return the non-val amount
        # Where counter is the first <counter> numbers of elements 
        # in the list that must not equal to val

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''