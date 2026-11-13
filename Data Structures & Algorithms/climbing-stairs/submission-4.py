class Solution:
    def climbStairs(self, n: int) -> int:
        #dp(i) = the number of ways to get from i to the top
        memo= {}
        def dp(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            ways = dp(i+1) + dp(i+2)
            memo[i] = ways
            return ways
        return dp(0)