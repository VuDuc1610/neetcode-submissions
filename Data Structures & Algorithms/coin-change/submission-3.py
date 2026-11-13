class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(cur):
            if cur > amount:
                return float('inf')
            if cur == amount:
                return 0
            if cur in memo:
                return memo[cur]
            temp = float('inf')
            for coin in coins:
                temp =  min(temp, 1 + dp(cur + coin))
            memo[cur] = temp
            return temp
        
        ans = dp(0)
        if ans == float('inf'):
            return -1
        return ans