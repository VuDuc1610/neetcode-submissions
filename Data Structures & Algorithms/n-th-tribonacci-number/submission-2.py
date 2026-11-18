class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(remain):
            if remain == 0 or remain == 1:
                return remain
            if remain == 2:
                return 1
            if remain in memo:
                return memo[remain]
            temp = 0 
            temp += dp(remain-1)+dp(remain-2)+dp(remain-3)
            memo[remain] = temp
            return temp
        return dp(n)