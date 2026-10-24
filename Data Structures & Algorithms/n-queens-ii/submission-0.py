class Solution:
    def totalNQueens(self, n: int) -> int:
        diaL, diaR, col = set(), set(), set()
        ans = 0

        def backtrack(idx):
            nonlocal ans
            if idx == n:
                ans += 1
                return
            
            for i in range(n):
                right = idx - i
                left = idx + i
                if (right not in diaR) and (left not in diaL) and (i not in col):
                    diaL.add(left)
                    diaR.add(right)
                    col.add(i)
                    backtrack(idx+1)

                    diaL.remove(left)
                    diaR.remove(right)
                    col.remove(i)

        backtrack(0)
        return ans
