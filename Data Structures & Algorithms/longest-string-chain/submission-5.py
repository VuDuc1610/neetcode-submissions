class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo = {}
        def dp(cur):
            if cur in memo:
                return memo[cur]
            ans = 1
            for j in range(len(cur)):
                shorter = cur[:j]+cur[j+1:]
                if shorter in words:
                    ans = max(ans, 1 + dp(shorter))
            memo[cur] = ans
            return ans
        
        best = 0
        for i in range(len(words)):
            best = max(best, dp(words[i]))
        return best