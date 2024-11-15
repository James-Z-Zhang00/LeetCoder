'''
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        start = False
        for i in range(len(s)-1,-1, -1):
            if s[i] == ' ' and start: 
                break
            elif s[i] == ' ':
                continue
            else: 
                start = True
                counter += 1
        return counter
    
'''
Time Complexity:    O(n)
Space Complexity:   O(n)
'''