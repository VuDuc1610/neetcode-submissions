class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0

        for i in range(1,len(s)):
            cur = s[i]
            num = abs(ord(s[i])-ord(s[i-1]))
            ans += num
        
        return ans