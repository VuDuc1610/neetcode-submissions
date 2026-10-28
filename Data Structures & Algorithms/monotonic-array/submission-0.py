class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = False
        if nums[0] < nums[-1]:
            increase = True
        
        for i in range(len(nums)-1):
            if increase and nums[i] > nums[i+1]:
                return False
            if not increase and nums[i] < nums[i+1]:
                return False
        return True