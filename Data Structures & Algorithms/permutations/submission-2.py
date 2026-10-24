class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(tmp, nums):
            if not nums:
                ans.append(tmp[:])
                return
            
            for i in range(len(nums)):
                tmp.append(nums[i])
                helper(tmp, nums[:i]+nums[i+1:])
                tmp.pop()
        
        helper([], nums)
        return ans