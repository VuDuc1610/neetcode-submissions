class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(temp, open, close):
            if len(temp) == 2*n:
                res.append(temp[:])
                return
            if close > open or open > n:
                return
            
            if open < n:
                helper(temp + "(", open + 1, close)
            if close < open:
                helper(temp + ")", open, close + 1)
            
        helper("", 0, 0)
        return res
