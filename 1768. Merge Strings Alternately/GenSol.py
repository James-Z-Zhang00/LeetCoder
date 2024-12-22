class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        String processing & array/list

        Handle unmatched string length
        '''
        i = 0
        res = ""
        while i < len(word1) and i < len(word2):
            res += word1[i]
            res += word2[i]
            i += 1
        if i == len(word1):
            res += word2[i:]
        if i == len(word2):
            res += word1[i:]
        return res