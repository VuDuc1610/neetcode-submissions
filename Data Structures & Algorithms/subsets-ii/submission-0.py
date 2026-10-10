class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def helper(index, tempList):
            if index == len(nums):
                ans.append(tempList[:])
                return
            
            tempList.append(nums[index])
            helper(index+1, tempList)
            tempList.pop()
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            helper(index+1, tempList)
        
        helper(0, [])
        return ans