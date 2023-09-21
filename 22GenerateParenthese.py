# 22. Generate Parenthese

'''
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''

# 35 ms 16.69 MB
# 91.29% 56.36%

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def deepthFirstSearch(left, right, s):
            # Stop case: if the amount is satisfied, add it to result
            if len(s) == n * 2:
                result.append(s)
                return
            # Recursive case I: if '(' is less than the given amount, keep add it
            if left < n:
                deepthFirstSearch(left+1, right, s + '(')
            # Recursive case II: if '(' is enough, start to add ')' 
            if right < left:
                deepthFirstSearch(left, right+1, s + ')')
        deepthFirstSearch(0,0,'')
        return result

'''
								   	(0, 0, '')
								 	    |	
									(1, 0, '(')  
								   /           \
							(2, 0, '((')      (1, 1, '()')
							   /                 \
						(2, 1, '(()')           (2, 1, '()(')
						   /                       \
					(2, 2, '(())')                (2, 2, '()()')
						      |	                             |
					res.append('(())')             res.append('()()')

                    THE FUNCTION WILL ADD SUFFICIENT '(' STRAIGHTAWAY THEN ADD ')' WHICH IS THE LEFT WING
                    AFTER COMPLETE THE PARANTHESIS THE LEFT WING WILL TRACE BACK
                    THEN (1,0,'(') WILL START TO EXECUTE `if right < left` TO MAKE (1,1,'()')
                    THEN CALL THE FUNCTION AGAIN, REACH `if left < n` TO MOVE TO (2,1,'()(')
                    CALL THE FUNCTION AGAIN, BUT THIS TIME REACH `if right < left`
                    ADD THE LAST ONE (2,2,'()()'), TRACE BACK.
'''
