# 17. Letter Combinations of a Phone Number

# UNFINISHED SEP. 19TH 2023
# FINISHED SEP. 20TH 2023

'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap  = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        combinations = []
        if len(digits) != 0:
            self.f(0, digits, combinations, phoneMap, '')
        return combinations

    def f(self, i, digits, combinations, phoneMap, curr):
        if len(curr) == len(digits):
            combinations.append(curr)
            return
        for j in range(len(phoneMap[int(digits[i])])):
            self.f(i + 1, digits, combinations, phoneMap, curr + phoneMap[int(digits[i])][j])

'''

# Re-written
# 35 ms 16.20 MB
# 76.58% 97.15%

class Solution:

    def letterCombinations(self, digits: str):

        # Number dictionary
        num_dic = {
            2:'abc', 3:'def', 4:'ghi', 5:'jkl',
            6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz',
        }
        # Final returning list
        result = []
        if len(digits) != 0:
            # Recursive function parameters:
            # 0: the index of the given digits (the first digit)
            # digits: all given digits
            # result: the returning list for my final answer
            # num_dic: which number associate to which letters
            # '': the carry, temporarily store the current possible letters before add to result
            self.recursive_func(0, digits, result, num_dic, '')
        return result
    
    def recursive_func(self, i, digits, result, num_dic, carry):
        # Stop case: when the length of carry (possible letters) reaches the same length as the given digit, stop
        if len(carry) == len(digits):
            result.append(carry)
            return
        # Recursive case & iteration: iterate through all possible letters of the current digit
        # Recursively call for the next digit until the last digit
        for j in range(len(num_dic[int(digits[i])])):
            self.recursive_func(i+1, digits, result, num_dic, carry+num_dic[int(digits[i])][j])

    # I feel the whole thing like a search-tree traverse, instead of binary tree, it has 3 or 4 paths for each node.

'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_d = {'2':['a','b','c'], 
                '3':['d','e','f'],
                '4':['g','h','i'], 
                '5':['j','k','l'], 
                '6':['m','n','o'], 
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        res = []
        def find_n(ind,sub):
            if len(sub) ==len(digits):
                res.append(sub[:])
                return
            # if ind >= len(digits):
            #     return 
            dig = digits_d[digits[ind]]
            for i in dig:
                sub.append(i)
                find_n(ind+1,sub)
                sub.pop()
        
        if len(digits) >0:
            find_n(0,[])
        else:
            return []
        res1 = []
        for i in res:
            res1.append("".join(i))
        return res1
'''

# Another recursion method, less recursion part
# 30 ms 16.16 MB
# 95.31% 97.15%

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Number dictionary
        num_dic = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz',
        }
        result = []

        def search_in_digits(ndx,temp):
            if len(temp) == len(digits):
                result.append(temp[:])
                return
            dig_str = num_dic[digits[ndx]]
            for i in dig_str:
                temp.append(i)
                search_in_digits(ndx+1,temp)
                temp.pop()
        
        if len(digits) >0:
            search_in_digits(0,[])
        else:
            return []
        res1 = []
        for i in result:
            res1.append("".join(i))
        return res1
    
# I improved the method above to use a string instead of list of char to get rid of the last part res1.append...
# But it made the program run slower
# 37 ms 16.22 MB
# 68.81% 81.05%
    
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Number dictionary
        num_dic = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz',
        }
        result = []

        def search_in_digits(ndx,temp):
            if len(temp) == len(digits):
                result.append(temp)
                return
            dig_str = num_dic[digits[ndx]]
            for i in dig_str:
                temp += i
                search_in_digits(ndx+1,temp)
                temp = temp[:-1]
        
        if len(digits) >0:
            search_in_digits(0,'')
        else:
            return ''

        return result