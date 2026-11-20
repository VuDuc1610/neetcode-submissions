class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(cur, index):
            if cur == amount:
                return 1
            if cur > amount:
                return 0
            if (cur, index) in memo:
                return memo[(cur, index)]
            ans = 0
            for i in range(index, len(coins)):
                ans += dp(cur+coins[i], i)
            memo[(cur,index)] = ans
            return ans
        return dp(0,0)