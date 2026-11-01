from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        pass
        ans = 0
        q = deque()
        def bfs(tmp):
            nonlocal ans
            while q:
                r, c = q.popleft()
                tmp += grid[r][c]
                ans = max(ans, tmp)
                grid[r][c] = 0
                directions = [(1,0), (0,1), (-1,0), (0, -1)]
                for i, j in directions:
                    nr = r + i
                    nc = c + j
                    if nr < 0 or nc < 0 or nr > len(grid)-1 or nc > len(grid[0])-1:
                        continue
                    if grid[nr][nc] == 0:
                        continue
                    q.append([nr,nc])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    q.append([i,j])
                    bfs(0)
        
        return ans


