class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                prod *= num
        
        if count > 1:
            return [0]*len(nums)


        ans = [1]*len(nums)
        for i in range(len(nums)):
            if count == 1:
                if nums[i] == 0:
                    ans[i] = prod
                else: ans[i] = 0
            else:
                ans[i] = prod // nums[i]
        return ans