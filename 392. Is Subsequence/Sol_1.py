class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        '''
        Two Pointers
        '''

        if len(s) > len(t): return False
        if s is '': return True

        counter = 0

        for c in t:
            if counter <= len(s) - 1 and s[counter] == c:
                counter += 1
        return counter == len(s)