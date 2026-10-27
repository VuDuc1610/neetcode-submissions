class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0

        def findStart():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return (i,j)
            return (-1,-1)
        
        def dfs(r, c):
            nonlocal ans
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            ans += 4

            for i, j in directions:
                nr = r + i
                nc = c + j

                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] == 0:
                    continue

                ans -= 1
                if grid[nr][nc] == 2:
                    continue
                
                grid[nr][nc] = 2
                dfs(nr, nc)


        r, c = findStart()
        grid[r][c] = 2
        dfs(r,c)
        return ans