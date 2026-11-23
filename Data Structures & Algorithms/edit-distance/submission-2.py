class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(i, j):
            if j == len(word2):
                return len(word1)-i
            if i == len(word1):
                return len(word2)-j
            if (i,j) in memo:
                return memo[(i,j)]

            if word1[i] == word2[j]:
                ans = dp(i+1,j+1)
            else:
                ans = 1 + min(dp(i+1,j+1), dp(i+1,j), dp(i,j+1))

            memo[(i,j)] = ans
            return ans
        return dp(0,0)