class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:   
        #lowerbound
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        
        if l == len(nums) or nums[l] != target:
            return [-1,-1]
        
        #upperbound
        i, j = 0, len(nums)
        while i < j:
            m = i + (j-i)//2
            if nums[m] > target:
                j = m
            else:
                i = m + 1

        return [l,i-1]