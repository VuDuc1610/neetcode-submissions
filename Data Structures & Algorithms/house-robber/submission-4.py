class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #dp(i) means max amount of money collected from the start to that position i (including i)
        memo = {}
        def dp(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            if i == 1:
                return nums[1]
            if i in memo:
                return memo[i]
            res = nums[i] + max(dp(i-2), dp(i-3))
            memo[i] = res
            return res 
        
        return max(dp(len(nums)-1), dp(len(nums)-2))
            