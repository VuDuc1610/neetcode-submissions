class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #dp(i) means max amount of money collected from the start to that position i (including i)
        memo = {}
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i in memo:
                return memo[i]
            res = max(nums[i] + dp(i-2), dp(i-1))
            memo[i] = res
            return res
        
        return dp(len(nums)-1)
            