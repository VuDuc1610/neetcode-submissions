class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)
        memo = [[-1]*n for _ in range(n)]
        def dp(l,r):
            if r - l < 2:
                return 0
            if memo[l][r] != -1:
                return memo[l][r]
            ans = 0
            for i in range(l+1, r):
                coins = arr[i]*arr[l]*arr[r]
                ans = max(ans, dp(l, i) + coins + dp(i,r))
            memo[l][r] = ans
            return ans
        
        return dp(0,n-1)