class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i,j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if (i,j) in memo:
                return memo[(i,j)]

            match = i < len(s) and (p[j] == "." or s[i] == p[j])

            if j + 1 < len(p) and p[j+1] == "*":
                ans = dp(i, j+2) or (match and dp(i+1,j))
            else:
                ans = match and dp(i+1,j+1)

            memo[(i,j)] = ans
            return ans
        
        return dp(0,0)