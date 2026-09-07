class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        nums.sort()
        for i in range(len(nums)-2):
            curr = nums[i]
            if i > 0 and curr == nums[i-1]:
                continue
            target = 0-curr
            left, right = i + 1, len(nums)-1

            while left < right:
                if nums[left] + nums[right] == target:
                    ans.append([curr, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return ans