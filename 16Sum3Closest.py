# 16. 3 Sum Closest

# 1579 ms 16.60 MB

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        # Sort the list in ascending order
        nums.sort()
        # Through the list
        for i in range(len(nums)-2):
            # Make a cursor pointing to the next position of the list (second smallest number)
            # Make a cursor pointing to the end of the list (largest number)
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                # If the sum is smaller than target, increase the sum by moving the left cursor to the next position
                if sum3 < target:
                    l += 1
                # If the sum is larger than target, decrease the sum by moving the right cursor to the previous position
                else:
                    r -= 1
                # Check which can give us a better result, save the result
                if abs(sum3 - target) < abs(closest - target):
                    closest = sum3
        return closest

# Improved time algorithm
# R/M: 593 ms 16.16 MB
# Beats: 77.20% 99.55%

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallest_difference = float('inf')
        result = 0
        for i in range(len(nums)-1):
            left_ptr, right_ptr = i + 1, len(nums) - 1
            while left_ptr < right_ptr:
                sum3 = nums[i] + nums[left_ptr] + nums[right_ptr]
                current_difference = abs(sum3 - target)
                if current_difference < smallest_difference:
                    smallest_difference = current_difference
                    result = sum3
                if sum3 == target:
                    return target
                elif sum3 < target:
                    left_ptr += 1
                else:
                    right_ptr -= 1
        return result




