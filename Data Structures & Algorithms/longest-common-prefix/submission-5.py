class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        ans = strs[0]

        for i in range(1, len(strs)):
            if not strs[i]:
                return ""
            cur = strs[i]
            for j in range(len(ans)):
                if j == len(cur) or ans[j] != cur[j]:
                    ans = ans[:j]
                    break
            if len(ans) == 0:
                return ""
        
        return ans
                