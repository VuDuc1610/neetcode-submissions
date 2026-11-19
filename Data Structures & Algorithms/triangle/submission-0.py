class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(level, i):
            if level == len(triangle):
                return 0
            if (level, i) in memo:
                return memo[(level, i)]
            tmp = triangle[level][i]
            ans = min(tmp + dp(level+1, i), tmp + dp(level+1, i+1))
            memo[(level,i)] = ans
            return ans
        
        return dp(0,0)