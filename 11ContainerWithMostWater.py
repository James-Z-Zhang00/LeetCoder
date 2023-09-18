# 11. Container With Most Water

# Time limit exceeded
# Time Complexity: O(n * n), Space Complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        for i in range(0,len(height)):
            for j in range(i+1, len(height)):
                currentArea = min(height[i], height[j]) * (j - i)
                result = max(result, currentArea)
        return result

# 599 ms 29.28 MB
# 61.26% 79.80%

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            result = max(result, currentArea)

            # Move the left or right cursor depending on the height
            # Basically we discard the lower height everytime in order to find the maximum area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result



