class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, cur):
            if i == len(nums):
                if cur == target:
                    return 1
                else:
                    return 0
            if (i,cur) in memo:
                return memo[(i,cur)]
            ways = dp(i+1, cur+nums[i]) + dp(i+1, cur-nums[i])
            memo[(i,cur)] = ways
            return ways
        
        return dp(0,0)