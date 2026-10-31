class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
                return 
            if image[r][c] != old:
                return
            
            image[r][c] = color

            direction = [(1,0), (0,1), (-1,0), (0, -1)]
            for i, j in direction:
                nr = r + i
                nc = c + j
                dfs(nr, nc)
        
        if color == image[sr][sc]:
            return image
        old = image[sr][sc]

        dfs(sr, sc)

        return image

