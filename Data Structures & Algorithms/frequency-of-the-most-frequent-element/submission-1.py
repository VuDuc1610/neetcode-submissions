class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, l, window = 0, 0, 0
        for i in range(len(nums)):
            window += nums[i]
            temp = nums[i]*(i-l+1)
            while temp - window > k:
                window -= nums[l]
                l += 1
                temp = nums[i] * (i-l+1)
            ans = max(ans, i-l+1)
        return ans