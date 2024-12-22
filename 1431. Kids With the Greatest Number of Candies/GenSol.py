class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        '''
        Array
        '''

        res = []

        for c in candies:
            if c+extraCandies >= max(candies): res.append(True)
            else: res.append(False)

        return res