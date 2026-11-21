class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dp(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            ans = 0
            for k in range(i,len(s)):
                if s[k] == t[j]:
                    ans += dp(k+1, j+1)
            memo[(i,j)] = ans
            return ans
        
        return dp(0,0)