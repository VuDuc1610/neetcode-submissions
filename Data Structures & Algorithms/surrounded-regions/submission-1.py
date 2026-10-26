class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(r, c):
            direction = [(1,0), (-1,0), (0,1), (0,-1)]

            for i, j in direction:
                nr = r + i
                nc = c + j

                if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]):
                    continue
                if board[nr][nc] == "X" or (nr, nc) in safe:
                    continue
                safe.add((nr,nc))
                dfs(nr, nc)

        safe = set()
        q = deque()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1):
                    safe.add((i,j)) 
                    q.append((i,j))
        
        while q:
            r, c = q.popleft()
            dfs(r,c)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in safe:
                    board[i][j] = "X"