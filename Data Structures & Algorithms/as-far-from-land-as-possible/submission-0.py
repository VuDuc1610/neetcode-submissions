from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        pass
        ans = 0
        visit = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visit += 1
                    q.append((i,j))
        if visit == 0 or visit == len(grid)*len(grid[0]):
            return -1
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for a, b in directions:
                    nr = r + a
                    nc = c + b
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        visit += 1
                        q.append((nr,nc))
            ans += 1

        return ans -1
