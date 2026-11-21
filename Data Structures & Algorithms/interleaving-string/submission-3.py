class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = [[None]*(len(s2)+1) for _ in range(len(s1)+1)]
        if len(s3) != len(s1)+len(s2):
            return False
        
        def dp(i,j):
            if i == len(s1) and j == len(s2):
                return True
            if memo[i][j] is not None:
                return memo[i][j]
            ans = False
            if i < len(s1) and s1[i] == s3[i+j]:
                ans = dp(i+1,j)
            if j < len(s2) and s2[j] == s3[i+j]:
                ans = dp(i,j+1)
            memo[i][j] = ans
            return ans
        
        return dp(0,0)