class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #dp[i]: cheapest u need to spend STARTING from that index
        duration = [1, 7, 30]
        memo = {}

        def helper(i):
            if i == len(days):
                return 0
            if i in memo:
                return memo[i]

            ans = float('inf')
            for k in range(3):
                j = i
                while j < len(days) and days[j] < days[i] + duration[k]:
                    j += 1
                ans = min(ans, costs[k] + helper(j))
            
            memo[i] = ans
            return ans
        
        return helper(0)
