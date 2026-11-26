class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(nums)-1:
                return 0
            best = float('inf')
            for idx in range(1, nums[i]+1):
                best = min(best, 1 + dp(i+idx))
            memo[i] = best
            return best
        return dp(0)