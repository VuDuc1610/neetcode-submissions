class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(k-1,len(nums)):
            window = nums[i]-nums[i-k+1]
            ans = min(ans, window)
        return ans