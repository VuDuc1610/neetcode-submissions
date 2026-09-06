class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        tempLeft = 1
        for i in range(1, len(nums)):
            tempLeft *= nums[i-1]
            ans[i] *= tempLeft

        tempRight = 1
        for i in range(len(nums)-2, -1, -1):
            tempRight *= nums[i+1]
            ans[i] *= tempRight
        return ans