class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        duration = [1,7,30]
        memo = {}
        def dp(i):
            if i == len(days):
                return 0
            if i in memo:
                return memo[i]
            
            temp = float('inf')
            for k in range(3):
                j = i
                while j < len(days) and days[j] < days[i] + duration[k]:
                    j += 1
                temp = min(temp, costs[k] + dp(j))
                
            memo[i] = temp
            return temp
        
        return dp(0)