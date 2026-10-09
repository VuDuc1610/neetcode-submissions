class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(index, temp, tempList):
            if temp > target:
                return
            if temp == target:
                ans.append(tempList[:])
                return
            
            for i in range(index, len(nums)):
                tempList.append(nums[i])
                helper(i, temp + nums[i], tempList)
                tempList.pop()
                
        
        helper(0, 0, [])
        return ans