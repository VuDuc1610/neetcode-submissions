class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums)//2

        def backtrack(cur, index):
            print(cur)
            if cur == target:
                return True
            if index > len(nums)-1 or cur > target:
                return False
            for i in range(index, len(nums)):
                cur += nums[i]
                if backtrack(cur, i+1):
                    return True
                cur -= nums[i]
            return False
        return backtrack(0, 0)