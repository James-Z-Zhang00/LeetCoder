class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert the input string to a character array.
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"
        
        # Loop to get the start and the end pointer closer
        while start < end:
            # Locate the first vowel on the left hand side
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            
            # Locate the first vowel on the right hand side
            while start < end and vowels.find(word[end]) == -1:
                end -= 1
            
            # Swap the vowels
            word[start], word[end] = word[end], word[start]
            
            # Move the pointers towards each other for the next checking
            start += 1
            end -= 1
        
        # Convert the character array back to a string and return the result
        return "".join(word)