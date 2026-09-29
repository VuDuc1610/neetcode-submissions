class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0
            
        l, count, window = 0, 0, 1
        
        for i in range(len(nums)):
            window *= nums[i]
            while window >= k:
                window /= nums[l]
                l += 1
            count += i - l + 1
        return count