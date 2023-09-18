# 5. Longest Palindromic Substring

class Solution:

    def longestPalindrome(self, s: str) -> str:
        result = ''
        # Nested for-loop to make 2 search cursors
        for i in range(0, len(s)):
            # Only search for longer substrings
            for j in range(i+1+len(result), len(s)+1):
                w = s[i:j]
                # If it's palindromic, update the result
                if w == w[::-1]:
                    result = w
        return result