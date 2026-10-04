class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        
        for c in hashMap.values():
            if c % 2 != 0:
                return False
        return True