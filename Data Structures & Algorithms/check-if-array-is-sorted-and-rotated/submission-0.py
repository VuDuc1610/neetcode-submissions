class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            if i == len(nums)-1:
                if nums[i] > nums[0]:
                    count += 1
            elif nums[i] > nums[i+1]:
                count += 1
        if count == 1:
            return True
        return False