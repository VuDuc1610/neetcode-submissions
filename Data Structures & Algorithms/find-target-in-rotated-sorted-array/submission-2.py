class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the min in the arr first:
        i, j = 0, len(nums)-1
        while i < j:
            m = i + (j-i)//2
            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m
        
        l,r = 0,len(nums)-1
        if nums[-1] == target:
            return len(nums)-1
        if nums[-1] > target:
            l = j
        if nums[-1] < target:
            r = j - 1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1