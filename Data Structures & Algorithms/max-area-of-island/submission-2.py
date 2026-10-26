class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 0
            if grid[r][c] == 0 or board[r][c]:
                return 0
            
            board[r][c] = True

            down = dfs(r+1, c)
            up = dfs(r-1, c)
            right = dfs(r, c+1)
            left = dfs(r, c-1)

            return 1 + down + up + right + left
        
        ans = 0
        row, col = len(grid), len(grid[0])
        board = [[False] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and board[i][j] == False:
                    ans = max(ans, dfs(i, j))
        
        return ans