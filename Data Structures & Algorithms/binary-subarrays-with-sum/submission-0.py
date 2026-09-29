class Solution:
    def atMost(self, nums, goal):
        l, ans, window = 0, 0, 0
        for i in range(len(nums)):
            window += nums[i]
            while l <= i and window > goal:
                window -= nums[l]
                l += 1
            ans += i - l + 1
        return ans
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums,goal)-self.atMost(nums,goal-1)