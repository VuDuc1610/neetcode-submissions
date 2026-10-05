class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        ans = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != val:
                count += 1
                ans += 1
            else:
                nums.remove(nums[i])
        return ans