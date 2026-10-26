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

                if r + 1 < len(grid) and grid[r+1][c] == 1:
                    fresh -= 1
                    grid[r+1][c] = 2
                    queue.append([r+1, c])
                if r - 1 >= 0 and grid[r-1][c] == 1:
                    fresh -= 1
                    grid[r-1][c] = 2
                    queue.append([r-1,c])
                if c + 1 < len(grid[0]) and grid[r][c+1] == 1:
                    fresh -= 1
                    grid[r][c+1] = 2
                    queue.append([r, c+1])
                if c - 1 >= 0 and grid[r][c-1] == 1:
                    fresh -= 1 
                    grid[r][c-1] = 2
                    queue.append([r, c-1])
        if fresh != 0:
            return -1
            
        return ans