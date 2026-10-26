class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i,j])
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                val = grid[r][c]

                if r + 1 < len(grid) and grid[r+1][c] == 2147483647:
                    grid[r+1][c] = val + 1
                    q.append([r+1,c])
                if r - 1 >= 0 and grid[r-1][c] == 2147483647:
                    grid[r-1][c] = val + 1
                    q.append([r-1,c])
                if c + 1 < len(grid[0]) and grid[r][c+1] == 2147483647:
                    grid[r][c+1] = val + 1
                    q.append([r,c+1])
                if c - 1 >= 0 and grid[r][c-1] and grid[r][c-1] == 2147483647:
                    grid[r][c-1] = val + 1
                    q.append([r,c-1])
