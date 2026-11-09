class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def backtrack(i):
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]
            if s[i] == "0":
                return 0

            ways = backtrack(i+1)
            if i + 1 < len(s) and int(s[i:i+2]) < 27:
                ways += backtrack(i+2)
            memo[i] = ways
            return ways
            
            return 0
        
        return backtrack(0)