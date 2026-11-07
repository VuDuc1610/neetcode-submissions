from collections import deque
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    border = False
                    q = deque()
                    q.append((i,j))

                    while q:
                        r, c = q.popleft()
                        if r < 0 or c < 0 or r > len(grid)-1 or c > len(grid[0])-1 or grid[r][c] == 1:
                            continue
                        if grid[r][c] == 0 and (r == 0 or c == 0 or r == len(grid)-1 or c == len(grid[0])-1):
                            border = True
                        grid[r][c] = 1
                        directions = [(1,0), (0,1), (-1,0), (0,-1)]
                        for a, b in directions:
                            nr = r + a
                            nc = c + b
                            q.append((nr,nc))
                    if not border:
                        ans += 1
        return ans
        
