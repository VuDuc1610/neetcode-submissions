class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans, cur = 0, 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                cur += nums[i]
            else:
                cur = nums[i]
            ans = max(ans, cur)
        return ans