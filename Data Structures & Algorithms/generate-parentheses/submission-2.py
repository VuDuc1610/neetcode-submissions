class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(tmp, close, open):
            if len(tmp) == 2*n:
                ans.append(tmp)
                return
            
            if open < n:
                backtrack(tmp + "(", close, open + 1)
            
            if close < open:
                backtrack(tmp + ")", close + 1, open)
            
        backtrack("", 0,0)

        return ans
