class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        memo = {}

        def dp(index):
            if index == len(words)-1:
                return 1
            if index in memo:
                return memo[index]
            cur = words[index]
            ans = 1
            for i in range(index+1, len(words)):
                newWord = words[i]
                if len(newWord) > len(cur) + 1:
                    continue
                for j in range(len(newWord)):
                    cutWord = newWord[:j] + newWord[j+1:]
                    if cutWord == cur:
                        ans = max(ans, 1 + dp(i))
            memo[index] = ans
            return ans
        
        best = 0
        for i in range(len(words)):
            best = max(best, dp(i))
        return best