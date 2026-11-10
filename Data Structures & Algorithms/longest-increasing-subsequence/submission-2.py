class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def helper(i):
            if i in memo:
                return memo[i]
            top = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    top = max(top, helper(j) + 1)
            memo[i] = top
            return top
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, helper(i))
        return ans