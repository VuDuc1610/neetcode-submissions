class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = [[temperatures[0],0]]
        for i in range(1, len(temperatures)):
            curr = temperatures[i]
            while stack and curr > stack[-1][0]:
                res = i - stack[-1][1]
                ans[stack[-1][1]] = res
                stack.pop()
            stack.append([curr,i])    
        return ans
