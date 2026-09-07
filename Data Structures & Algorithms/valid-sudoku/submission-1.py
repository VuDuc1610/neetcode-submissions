class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            my_set = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in my_set:
                    return False
                my_set.add(board[i][j])
        
        for j in range(len(board)):
            my_set = set()
            for i in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue
                if board[i][j] in my_set:
                    return False
                my_set.add(board[i][j])
        
        for i in range(0,9):
            my_set = set()
            for m in range(0,3):
                for n in range(0,3):
                    row = (i // 3) * 3 + m
                    column = (i % 3) * 3 + n
                    num = board[row][column]
                    if num == ".":
                        continue
                    if num in my_set:
                        return False
                    my_set.add(num)
        return True

