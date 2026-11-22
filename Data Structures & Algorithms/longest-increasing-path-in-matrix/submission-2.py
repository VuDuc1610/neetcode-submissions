class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1)] 
        memo = [[-1]*len(matrix[0]) for _ in range(len(matrix))]
        def dp(r, c):
            isBiggest = True
            if memo[r][c] != -1:
                return memo[r][c]
            for i, j in directions:
                nr = r + i
                nc = c + j
                if nr < 0 or nr >= len(matrix) or nc < 0 or nc >= len(matrix[0]):
                    continue
                if matrix[nr][nc] > matrix[r][c]:
                    isBiggest = False 
            if isBiggest:
                return 1
            
            ans = 0
            for i, j in directions:
                nr = r + i
                nc = c + j
                if nr < 0 or nr >= len(matrix) or nc < 0 or nc >= len(matrix[0]):
                    continue
                if matrix[nr][nc] > matrix[r][c]:
                    ans = max(ans, 1 + dp(nr, nc))
            memo[r][c] = ans
            return ans
        
        best = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                best = max(best, dp(i, j))
        return best
            