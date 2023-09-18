# 4. Median of Two Sorted Arrays

class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        temp = []
        # Simply sort both arrays
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                temp.append(nums1[p1])
                p1 += 1
            else:
                temp.append(nums2[p2])
                p2 += 1
        
        # Consider 2 arrays are different in length
        while p1 < len(nums1):
            temp.append(nums1[p1])
            p1 += 1
        while p2 < len(nums2):
            temp.append(nums2[p2])
            p2 += 1
        
        # Get the result
        if len(temp) % 2 == 0:
            middle = len(temp) // 2
            median = (temp[middle] + temp[middle-1]) / 2
        else:
            median = float(temp[len(temp)//2])

        return median