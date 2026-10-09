class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        index = 0
        
        def helper(index, nums, tempList):
            if index == len(nums):
                ans.append(tempList[:])
                return
            tempList.append(nums[index])
            helper(index+1, nums, tempList)
            tempList.pop()
            helper(index+1, nums, tempList)
        
        helper(0, nums, [])
        
        return ans