class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}
        def dp(index):
            if index == len(arr):
                return 0
            if index in memo:
                return memo[index]
            ans = 0
            for i in range(index, min(k+index, len(arr))):
                tmp = arr[index:i+1]
                cur = max(tmp)*len(tmp) + dp(i+1)
                ans = max(ans, cur)
            memo[index] = ans
            return ans
        
        return dp(0)