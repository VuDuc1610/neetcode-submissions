class Solution:
    def numDecodings(self, s: str) -> int:
        ans = 0
        memo = {}

        def backtrack(i):
            nonlocal ans
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]

            num1 = s[i]
            num2 = s[i:i+2]
            if num1 != "0":
                case1 = backtrack(i+1)
                case2 = 0
                if i + 1 < len(s) and int(num2) < 27:
                    case2 = backtrack(i+2)
                memo[i] = case1+case2
                return case1+case2
            
            return 0
        
        return backtrack(0)