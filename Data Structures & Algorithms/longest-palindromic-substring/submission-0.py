class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            l1, r1 = i,i
            while l1 >= 0 and r1 < len(s):
                if s[l1] != s[r1]:
                    break
                if r1-l1+1 > len(ans):
                    ans = s[l1:r1+1]
                l1 -= 1
                r1 += 1
            
            l2, r2 = i, i + 1
            while l2 >= 0 and r2 < len(s):
                if s[l2] != s[r2]:
                    break
                if r2-l2+1 > len(ans):
                    ans = s[l2:r2+1]
                l2 -= 1
                r2 += 1
        
        return ans