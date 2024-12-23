class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        s2 = ""
        for c in s:
            if c in ['a','e','i','o','u','A','E','I','O','U']:
                vowels.append(c)
        vowels.reverse()

        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                s2 += vowels[0]
                vowels = vowels[1:]
            else:
                s2 += s[i]
        return s2