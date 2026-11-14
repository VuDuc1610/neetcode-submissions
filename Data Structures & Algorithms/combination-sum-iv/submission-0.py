class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            temp = 0
            for num in nums:
                temp += dp(i-num)
            memo[i] = temp
            return temp
            
        return dp(target)