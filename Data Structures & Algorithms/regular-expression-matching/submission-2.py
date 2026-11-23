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

            ans1, ans2, ans3 = False, False, False
            cur = ""
            if i < len(s):
                cur = s[i]

            if j + 1 < len(p) and p[j+1] == "*":
                if cur == "" or (p[j] != "." and cur != p[j]):
                    ans1 = dp(i, j+2)
                else:
                    ans2 = dp(i,j+2) or dp(i+1, j)
            else:
                if cur != "" and (cur == p[j] or p[j] == "."):
                    ans3 = dp(i+1, j+1)
                else:
                    return False
            ans = ans1 or ans2 or ans3
            memo[(i,j)] = ans
            return ans
        
        return dp(0,0)