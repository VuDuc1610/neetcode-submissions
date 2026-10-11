class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0

        for i in range(1,len(s)):
            cur = s[i]
            num = abs(ord(s[i])-ord(s[i-1]))
            if num < 0:
                num = -num
            ans += num
        
        return ans