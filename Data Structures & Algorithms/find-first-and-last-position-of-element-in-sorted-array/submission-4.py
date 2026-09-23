class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        if len(nums) == 0:
            return ans
        
        #lowerbound
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        
        if l < len(nums) and nums[l] == target:
            ans[0] = l
        else:
            return [-1,-1]
        
        #upperbound
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        ans[1] = l-1

        return ans