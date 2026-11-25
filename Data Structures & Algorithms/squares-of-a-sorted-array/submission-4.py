class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        l, r = 0, n-1
        idx = n-1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans[idx] = nums[l]*nums[l]
                l += 1
            else:
                ans[idx] = nums[r]*nums[r]
                r -= 1
            idx -= 1
        return ans