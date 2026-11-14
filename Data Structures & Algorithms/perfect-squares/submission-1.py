import sys
sys.setrecursionlimit(200000)
class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def dp(remain):
            if remain == 0:
                return 0
            if remain in memo:
                return memo[remain]
            k = 1
            temp = float('inf')
            while k*k <= remain:
                temp = min(temp, 1 + dp(remain - k*k))
                k += 1
            memo[remain] = temp
            return temp
        
        return dp(n)