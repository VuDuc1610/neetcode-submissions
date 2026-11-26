class Solution:
    def jump(self, nums: List[int]) -> int:
        jump, end, furthest = 0,0,0

        for i in range(len(nums)-1):
            furthest = max(furthest, i + nums[i])
            if i == end:
                end = furthest
                jump += 1
        return jump