class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #first element that is greater or equal to target
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        if l < len(nums) and nums[l] == target:
            return l
        return -1