class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(tempList, nums):
            if not nums:
                ans.append(tempList[:])
                return
            
            for i in range(len(nums)):
                num = nums[i]
                tempList.append(num)
                lst = nums[:]
                lst.remove(num)
                helper(tempList,lst)
                tempList.pop()
        
        helper([], nums)
        return ans