class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i == len(nums):
                return 0
            if i in memo:
                return memo[i]
            temp = max(nums[i], nums[i] + dp(i+1))
            memo[i] = temp
            return temp
        
        ans = float('-inf')
        for i in range(len(nums)):
            ans = max(ans, dp(i))
        return ans
