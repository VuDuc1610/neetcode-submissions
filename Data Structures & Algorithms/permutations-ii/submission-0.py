class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def helper(tmp, nums):
            if not nums:
                ans.append(tmp[:])
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                num = nums[i]
                tmp.append(num)
                helper(tmp, nums[:i] + nums[i+1:])
                tmp.pop()
        
        helper([], nums)

        return ans