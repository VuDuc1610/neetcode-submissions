class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1]*len(coins) for _ in range(amount + 1)]
        def dp(cur, index):
            if cur == amount:
                return 1
            if cur > amount:
                return 0
            if memo[cur][index] != -1:
                return memo[cur][index]
            ans = 0
            for i in range(index, len(coins)):
                ans += dp(cur+coins[i], i)
            memo[cur][index] = ans
            return ans
        return dp(0,0)