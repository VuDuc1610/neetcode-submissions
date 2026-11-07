class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        count = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                cur = grid2[i][j]
                if cur == 1:
                    sink = False
                    stack = [(i,j)]

                    while stack:
                        r, c = stack.pop()
                        if r < 0 or c < 0 or r > len(grid1)-1 or c > len(grid1[0])-1 or grid2[r][c] == 0:
                            continue
                        if grid1[r][c] == 0:
                            sink = True
                        grid2[r][c] = 0
                        for a, b in directions:
                            nr = r + a
                            nc = c + b
                            stack.append((nr,nc))
                    if not sink:
                        count += 1
        return count