class Solution:
    def numDecodings(self, s: str) -> int:
        #dp(i) means number of counts starting from i till the end
        memo = {}
        def dp(i):
            if i == len(s):
                return 1
            if i >= len(s):
                return 0
            if i in memo:
                return memo[i]
            temp = 0
            if s[i:i+1] != "0":
                temp += dp(i+1)
                if int(s[i:i+2]) < 27:
                    temp += dp(i+2)
            memo[i] = temp
            return temp
        
        return dp(0)