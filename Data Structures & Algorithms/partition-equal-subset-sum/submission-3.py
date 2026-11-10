class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #if there is no memo, answer just like normal backtrack problem
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums)//2
        memo = {}

        def backtrack(cur, index):
            if cur == target:
                return True
            if index > len(nums)-1 or cur > target:
                return False
            if (cur, index) in memo:
                return memo[(cur, index)]
            for i in range(index, len(nums)):
                if backtrack(cur + nums[i], i+1):
                    memo[(cur+nums[i], i+1)] = True
                    return True
            
            memo[(cur+nums[i], i+1)] = True
            return False
        return backtrack(0, 0)