class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, idx):
            if idx == len(word):
                return True
            if row >= len(board) or col >=len(board[0]) or row < 0 or col < 0 or board[row][col] != word[idx]:
                return False
            
            temp = board[row][col]
            board[row][col] = "#"
            found = dfs(row-1, col, idx + 1) or dfs(row+1, col, idx + 1) or dfs(row, col-1, idx + 1) or dfs(row, col+1, idx + 1)

            board[row][col] = temp

            return found
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        return False
        
                