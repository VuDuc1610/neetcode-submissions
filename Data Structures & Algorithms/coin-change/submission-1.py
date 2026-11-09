class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def helper(remain):
            if remain < 0:
                return float('inf')
            if remain == 0:
                return 0
            if remain in memo:
                return memo[remain]
            
            ans = float('inf')
            for coin in coins:
                temp = helper(remain-coin)
                ans = min(ans, 1 + temp)
            memo[remain] = ans

            return ans

        answer = helper(amount)
        if answer == float('inf'):
            return -1
        return answer