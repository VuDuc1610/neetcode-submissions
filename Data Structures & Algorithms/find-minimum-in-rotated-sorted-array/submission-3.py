class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find minimum inside nums, so instead of compare to a target, compare to nums[j]
        #the statement else guarantee to be True (nums[mid] <= nums[j]) => r can be len-1
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]