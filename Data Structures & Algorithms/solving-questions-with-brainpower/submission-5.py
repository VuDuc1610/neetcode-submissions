class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0]*(len(questions)+1)
        for i in range(len(questions)-1, -1, -1):
            points = questions[i][0]
            temp = i + questions[i][1] + 1
            if temp >= len(dp):
                temp = 0
            dp[i] = max(dp[i+1], points + dp[temp])        

        return max(dp)