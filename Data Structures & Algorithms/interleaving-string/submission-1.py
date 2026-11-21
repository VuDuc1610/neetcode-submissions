class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        if len(s3) != len(s1)+len(s2):
            return False
        def dp(i,j):
            if i == len(s1) and j == len(s2):
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            ans1,ans2 = False, False
            if i < len(s1) and s1[i] == s3[i+j]:
                ans1 = dp(i+1,j)
            if j < len(s2) and s2[j] == s3[i+j]:
                ans2 = dp(i,j+1)
            memo[(i,j)] = ans1 or ans2
            if ans1 or ans2:
                return True
            return False
        
        return dp(0,0)