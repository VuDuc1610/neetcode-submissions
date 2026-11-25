class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        l, r = 0, len(nums)-1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans.append(nums[l]*nums[l])
                l += 1
            else:
                ans.append(nums[r]*nums[r])
                r -= 1
        res = []
        for i in range(len(ans)-1, -1, -1):
            res.append(ans[i])
        return res