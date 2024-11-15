'''
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        
        if not words:
            return 0
        
        return len(words[-1])

'''
Time Complexity:    O(n)
Space Complexity:   O(n)
'''