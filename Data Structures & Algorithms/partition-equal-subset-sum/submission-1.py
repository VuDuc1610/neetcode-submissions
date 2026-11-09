class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums)//2

        def backtrack(cur, index):
            if cur == target:
                return True
            if index > len(nums)-1 or cur > target:
                return False
            for i in range(index, len(nums)):
                if backtrack(cur + nums[i], i+1):
                    return True
            return False
        return backtrack(0, 0)