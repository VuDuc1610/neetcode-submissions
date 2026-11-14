import sys
sys.setrecursionlimit(200000)
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        memo = {}
        def dp(i):
            if i == len(nums):
                return True
            if i in memo:
                return memo[i]

            potential1, potential2 = False, False
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                potential1 = dp(i+2)
            
            if i + 2 < len(nums) and (nums[i] == nums[i+1] == nums[i+2] or (nums[i+2]-nums[i+1] == 1 and nums[i+1]-nums[i+0] == 1)):
                potential2 = dp(i+3)
        
            if potential1 or potential2:
                memo[i] = True
                return True
            
            memo[i] = False
            return False
        
        return dp(0)
