class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i,j,arr):
            directions = [(1,0), (-1,0), (0,-1), (0,1)]
            for x, y in directions:
                r, c = i + x, j + y
                if r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]):
                    continue
                if not arr[r][c] and heights[r][c] >= heights[i][j]:
                    arr[r][c] = True
                    dfs(r,c, arr)
            

        ans = []
        pac = [[False] * len(heights[0]) for _ in range(len(heights))]
        atl = [[False] * len(heights[0]) for _ in range(len(heights))]

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    pac[i][j] = True
                    dfs(i,j, pac)
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == len(heights)-1 or j == len(heights[0])-1:
                    atl[i][j] = True
                    dfs(i,j, atl)
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pac[i][j] and atl[i][j]:
                    ans.append([i,j])

        return ans
                

                