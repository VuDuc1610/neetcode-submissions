class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in myMap:
                return [myMap[temp], i]
            myMap[nums[i]] = i 
        return []