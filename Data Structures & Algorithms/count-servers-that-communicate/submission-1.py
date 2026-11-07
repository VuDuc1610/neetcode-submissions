class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = {i: [] for i in range(len(grid))}
        col = {i: [] for i in range(len(grid[0]))}

        ans = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row[i].append((i,j))
                    col[j].append((i,j))

        for val in row.values():
            if len(val) <= 1:
                continue
            for pair in val:
                if pair not in ans:
                    ans.add(pair)
        
        for val in col.values():
            if len(val) <= 1:
                continue
            for pair in val:
                if pair not in ans:
                    ans.add(pair)
        return len(ans)
        