class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i,j])

        direction = [(1,0), (-1,0), (0,1), (0, -1)]
        
        while q:
            r, c = q.popleft()

            for i, j in direction:
                newRow = r + i
                newCol = c + j

                if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]):
                    continue
                if grid[newRow][newCol] != 2147483647:
                    continue
                grid[newRow][newCol] = grid[r][c] + 1
                q.append([newRow, newCol])
