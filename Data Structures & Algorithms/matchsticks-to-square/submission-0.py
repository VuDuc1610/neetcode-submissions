class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        parameter = sum(matchsticks)
        if parameter % 4 != 0:
            return False
        side = parameter // 4
        buckets = [0]*4

        def helper(idx):
            if idx == len(matchsticks):
                return True
            
            if matchsticks[idx] > side:
                return False
            
            for i in range(len(buckets)):
                if buckets[i] + matchsticks[idx] <= side:
                    buckets[i] += matchsticks[idx]
                    if helper(idx+1):
                        return True
                    buckets[i] -= matchsticks[idx]
                    if buckets[i] == 0:
                        break
            
            return False
        
        return helper(0)