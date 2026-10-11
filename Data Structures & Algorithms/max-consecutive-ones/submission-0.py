class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        temp = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == 1:
                temp += 1
                ans = max(ans, temp)
            else:
                temp = 0
        return ans