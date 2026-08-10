class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            valid = set()
            for c in row:
                if c != '.' and c not in valid:
                    valid.add(c)
                elif c != '.' and c in valid:
                    return False
        
        # check columns
        for row in range(len(board)):
            valid = set()
            for col in range(len(board)):
                c = board[col][row]
                if c != '.' and c not in valid:
                    valid.add(c)
                elif c != '.' and c in valid:
                    return False          

        actions = [
            [-1,-1], [-1,0], [-1, 1], [0,-1], [0,0], [0,1],[1,-1],[1,0],[1,1]
        ]
        # check squares
        for i in [1,4,7]:
            for j in [1, 4, 7]:
                valid = set()
                for a in actions:
                    x = a[0]
                    y = a[1]
                    c = board[i + x][j + y]
                    if c != '.' and c not in valid:
                        valid.add(c)
                    elif c != '.' and c in valid:
                        return False           
        return True
