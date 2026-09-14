class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        ptr = 0
        ans = 0
        for i in range(1,len(prices)):
            if prices[i] <= prices[ptr]:
                ptr = i
            else:
                ans = max(ans, prices[i]-prices[ptr])
        return ans
            