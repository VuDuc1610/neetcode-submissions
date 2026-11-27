class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def bfs(i,j):
            count, total = 0, 0
            for r, c in direction:
                nr = r + i
                nc = c + j
                if 0 <= nr < len(img) and 0 <= nc < len(img[0]):
                    count += 1
                    total += img[nr][nc]
            if count == 0:
                return total
            return total//count

        direction = [(0,0), (1,0), (0,1), (-1,0), (0,-1),
                     (1,1), (1,-1), (-1,1), (-1,-1)]
        ans = [[0]*len(img[0]) for _ in range(len(img))]
        
        for i in range(len(img)):
            for j in range(len(img[0])):
                ans[i][j] = bfs(i,j)
        return ans
    

