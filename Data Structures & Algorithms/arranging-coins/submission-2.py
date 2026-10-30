class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0

        while n-ans > 0:
            ans += 1
            n -= ans
        
        return ans