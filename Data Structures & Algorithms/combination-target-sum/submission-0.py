class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(index, temp, tempList):
            if temp > target or index >= len(nums):
                return
            if temp == target:
                ans.append(tempList[:])
                return
            
            for i in range(index, len(nums)):
                tempList.append(nums[i])
                temp += nums[i]
                helper(i, temp, tempList)
                tempList.pop()
                temp -= nums[i]
                
        
        helper(0, 0, [])
        return ans