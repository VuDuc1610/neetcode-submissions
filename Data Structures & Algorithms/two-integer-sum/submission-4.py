class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #key = the num, value = index
        hasie = {}
        for i in range(len(nums)):
            remain = target-nums[i]
            if remain in hasie:
                return [hasie[remain], i]
            hasie[nums[i]] = i
         