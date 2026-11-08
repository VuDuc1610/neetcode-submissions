class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        #dp(i) = answer of the question at the position i
        copy1 = nums[:len(nums)-1]
        copy2 = nums[1:]
        def dp(i, lst, memo):
            if i == 0:
                return lst[0]
            if i == 1:
                return max(lst[0], lst[1])
            if i in memo:
                return memo[i]
            res = max(dp(i-1, lst, memo), lst[i] + dp(i-2, lst, memo))
            memo[i] = res
            return res
        
        LEN = len(copy1)
        return max(dp(LEN-1, copy1, {}), dp(LEN-1, copy2, {}))
