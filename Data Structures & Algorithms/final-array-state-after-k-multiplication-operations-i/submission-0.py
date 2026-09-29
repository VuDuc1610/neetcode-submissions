class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            minIndex = 0
            minNum = float('inf')
            for i in range(len(nums)-1, -1, -1):
                if minNum >= nums[i]:
                    minNum = nums[i]
                    minIndex = i
            nums[minIndex] *= multiplier
            k -= 1
        return nums
            