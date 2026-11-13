class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp(i) means max money from i to the end
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            temp = max(nums[i] + dp(i+2), dp(i+1))
            memo[i] = temp
            return temp
        return dp(0)