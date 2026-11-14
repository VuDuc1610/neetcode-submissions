import sys
sys.setrecursionlimit(200000)

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        
        def dp(i):
            if i >= len(questions):
                return 0
            if i in memo:
                return memo[i]
            temp = max(questions[i][0] + dp(i+questions[i][1]+1), dp(i+1))
            memo[i] = temp
            return temp
        
        return dp(0)
