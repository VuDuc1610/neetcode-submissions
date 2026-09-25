class Solution:
    def check(self, mid, nums, k):
        tempArr, tempSum = 1, 0
        for i in range(len(nums)):
            tempSum += nums[i]
            if tempSum > mid:
                tempArr += 1
                tempSum = nums[i]
        return tempArr
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + (r-l)//2
            count = self.check(mid, nums, k)
            if count > k:
                l = mid + 1
            else:
                r = mid
        return l