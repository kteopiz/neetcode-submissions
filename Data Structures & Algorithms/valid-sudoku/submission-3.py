class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows
        for row in board:
            seen = set()
            for n in row:
                if not n.isnumeric():
                    continue
                if n in seen:
                    return False
                seen.add(n)
        
        print('thru rows')
        # cols
        for col in range(9):
            seen = set()
            for row in range(9):
                n = board[row][col]
                print(n, 'going in ', seen)
                if not n.isnumeric():
                    continue
                if n in seen:
                    return False
                seen.add(n)
            
        print('thru cols')
            
        # boxes from middles
        # 8 directions from the middle
        dirs = [
            (-1,-1),
            (-1,0),
            (-1,1),
            (0,1),
            (1,1),
            (1,0),
            (1,-1),
            (0,-1)
        ]

        for row in [1, 4, 7]:
            for col in [1, 4, 7]:
                seen = set()
                for x,y in dirs:
                    n = board[row + x][col + y]
                    if not n.isnumeric():
                        continue
                    if n in seen:
                        return False
                    seen.add(n)
        
        return True


        