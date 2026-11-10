class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #tabulation
        dp = [1]*len(nums)
        

        for i in range(len(nums)-1, -1, -1):
            cur = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > cur:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)