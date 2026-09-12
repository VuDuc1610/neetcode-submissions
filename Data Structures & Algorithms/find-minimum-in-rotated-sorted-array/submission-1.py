class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        if nums[i] <= nums[j]:
            return nums[i]
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[mid-1]:
                if nums[mid] > nums[-1]:
                    i = mid + 1
                else: 
                    j = mid - 1
        return -1