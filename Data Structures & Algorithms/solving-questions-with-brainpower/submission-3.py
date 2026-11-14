class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #dp(i) means the highest points gathered until i
        dp = [0]*len(questions)
        dp[-1] = questions[-1][0]
        for i in range(len(dp)-2, -1, -1):
            points = questions[i][0]
            temp = i + questions[i][1] + 1
            if temp >= len(questions):
                temp = 0
            dp[i] = max(dp[i+1], points + dp[temp])        

        return max(dp)