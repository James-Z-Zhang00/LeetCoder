# 6. Zigzag Conversion

# THE FIRST MODEL ANSWER
# Runtime: 71 ms    Memory: 16.50 MB

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        nel = len(s)
        i = 0
        j = 0
        moving = 0
        temp = []
        while j < len(s):
            if i == 0:
                moving += 1
            else:
                moving -= 1

            if moving == numRows:
                i = 1
            elif moving <= 1:
                i = 0

            if j < numRows:
                temp.append([s[j]])
            else:
                temp[moving-1].append(s[j])
                
            j += 1

        word = ""
        for t in temp:
            word += "".join(t)
        return word
    
# THE SELF IMPROVED ANSWER
# Runtime: 60 ms    Memory: 16.41 MB

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 1
        j = 0
        moving = 0
        temp = []
        while j < len(s):
            moving += i

            if moving == numRows:
                i = -i
            elif moving <= 1 and j >= numRows:
                i = -i

            if j < numRows:
                temp.append([s[j]])
            else:
                temp[moving-1].append(s[j])
                
            j += 1

        word = ""
        for t in temp:
            word += "".join(t)
        return word
    
# THE SELF IMPROVED ANSWER ANOTHER
# Runtime: 57 ms    Memory: 16.35 MB

class Solution:

    def convert(self, s: str, numRows: int) -> str:
        i = -1 # The direction (increment or decrement of moving variable)
        j = 0 # The index of the given string as we go through the string
        moving = numRows # The number to indicate which row to add the next char when goes throgh the given string
        temp = [] # The list holds the matrix of chars, each string is a column in the matrix
        while j < len(s):
            if j < numRows:
                # For the first column, simply add chars as normal until the last row
                temp.append([s[j]])
            else:
                moving += i
                # If the next adding position is the top or the bottom row
                # Swap the direction of moving variable (+= 1 OR -= 1)
                # It supposed to moving between middle rows
                if moving == numRows or moving <= 1: i = -i
                # Add the char to the position moving-1 to match the index of the list
                temp[moving-1].append(s[j])
            # Go to the next char of the given string
            j += 1

        result = ""
        for t in temp:
            # Sum the result up
            result += "".join(t)
        return result