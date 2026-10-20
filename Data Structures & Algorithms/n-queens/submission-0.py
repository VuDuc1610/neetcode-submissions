class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        diagonalL, diagonalR, cols = set(), set(), set()
        ans = []
        board = []
        for i in range(n):
            board.append(["."] * n)
        
        def helper(row):
            if row == n:
                temp = []
                for r in board:
                    temp.append("".join(r))
                ans.append(temp)
                return
            
            for i in range(n):
                right = row-i
                left = row+i
                if (right not in diagonalR) and (left not in diagonalL) and i not in cols:
                    board[row][i] = "Q"
                    diagonalL.add(left)
                    diagonalR.add(right)
                    cols.add(i)
                    
                    helper(row+1)
                    
                    board[row][i] = "."
                    diagonalL.remove(left)
                    diagonalR.remove(right)
                    cols.remove(i)
        
        helper(0)
        return ans

