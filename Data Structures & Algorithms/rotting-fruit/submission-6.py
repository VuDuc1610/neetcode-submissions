class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        queue = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur = grid[i][j]
                if cur == 1:
                    fresh += 1
                elif cur == 2:
                    queue.append([i, j])

        while queue and fresh > 0:
            ans += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                directions = [(0,1), (1,0), (-1,0), (0,-1)]
                for a,b in directions:
                    nr = r + a
                    nc = c + b
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] != 1:
                        continue
                    fresh -= 1
                    grid[nr][nc] = 2
                    queue.append([nr,nc])
        if fresh != 0:
            return -1
            
        return ans