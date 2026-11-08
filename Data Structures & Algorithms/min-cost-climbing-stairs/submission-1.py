class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def helper(i):
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            if i in memo:
                return memo[i]
            res = cost[i] + min(helper(i-1), helper(i-2))
            memo[i] = res
            return res
        
        stairs = len(cost)
        return min(helper(stairs-1), helper(stairs-2))