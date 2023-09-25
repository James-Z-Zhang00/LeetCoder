# 8. String to Integer
# Failed in the case s="-91283472332" on LeetCode compiler

'''
Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        final_result = 0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        negative = False
        for c in s:
            if c.isdigit():
                result += c
            elif c == '-':
                negative = True
            elif c == ' ':
                continue
            else:
                break
        if result == '':
            return 0
        final_result = -int(result) if negative else int(result)
        if final_result < INT_MIN: return INT_MIN
        elif final_result > INT_MAX: return INT_MAX
        else: return final_result

# Other answer from solution pool

class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':  # skipping space characters at the beginning
            i += 1

        positive = 0
        negative = 0

        if i < n and s[i] == '+':
            positive += 1  # number of positive signs at the start in string
            i += 1

        if i < n and s[i] == '-':
            negative += 1  # number of negative signs at the start in string
            i += 1

        ans = 0.0

        while i < n and '0' <= s[i] <= '9':
            # converting character to integer
            ans = ans * 10 + (ord(s[i]) - ord('0'))
            i += 1

        if negative > 0:  # if negative sign exists
            ans = -ans

        if positive > 0 and negative > 0:  # if both +ve and -ve signs exist, Example: +-12
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if ans > INT_MAX:  # if ans > 2^31 - 1
            ans = INT_MAX

        if ans < INT_MIN:  # if ans < -2^31
            ans = INT_MIN

        return int(ans)

# Self re-do 
# 37 ms 16.28 MB


class Solution:
    def myAtoi(self, s):
        # Get rig of whitespaces at front and back of the given string
        # i is the starting position (index) of the string
        # Both positive and negative signs are False by default
        s, i, positive, negative = s.strip(), 0, False, False
        # n is the new length of the string after strip
        # INT_MAX and INT_MIN are the given limit for final answer
        n, INT_MAX, INT_MIN, result = len(s), 2**31 - 1, -2**31, 0

        # Detect the signs
        if i < n and s[i] == '+':
            positive = True
            i += 1

        if i < n and s[i] == '-':
            negative = True
            i += 1

        while i < n and '0' <= s[i] <= '9':
            # Converting character to integer
            # These can ignore the leading 0s since 0 * 10 is 0
            result = result * 10 + (ord(s[i]) - ord('0'))
            i += 1

        if positive and negative:
            return 0
        if negative:
            result = -result

        return result if INT_MIN <= result <= INT_MAX else (INT_MAX if result > INT_MAX else INT_MIN)
