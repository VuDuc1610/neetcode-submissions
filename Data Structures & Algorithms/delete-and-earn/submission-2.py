class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i == len(nums):
                return 0
            if i in memo:
                return memo[i]
            tmp = nums[i]
            end = i
            while end+1 < len(nums) and nums[end+1] == nums[end]:
                tmp += nums[end]
                end += 1
            j = end + 1
            while j < len(nums) and nums[j] == nums[i]+1:
                j += 1
            
            ans = max(tmp + dp(j), dp(end+1))
            memo[i] = ans
            return ans
        
        nums.sort()
        return dp(0)
