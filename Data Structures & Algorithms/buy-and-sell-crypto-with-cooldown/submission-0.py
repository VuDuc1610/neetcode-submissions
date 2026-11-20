class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in memo:
                return memo[(i,buy)]
            ans = 0
            if buy == -1:
                ans = max(dp(i+1,prices[i]), dp(i+1,-1))
            else:
                ans = max((prices[i]-buy + dp(i+2, -1), dp(i+1, buy)))
            memo[(i,buy)] = ans
            return ans
        
        return dp(0,-1)