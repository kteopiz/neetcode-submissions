class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top < bot:
            m = (top + bot) // 2

            if target < matrix[m][0]:
                bot = m - 1
            elif target > matrix[m][-1]:
                top = m + 1
            else:
                top = m
                bot = m
        
        searchRow = matrix[top]
        l, r = 0, len(searchRow) - 1

        while l <= r:
            m  = (l +  r) // 2

            if target < searchRow[m]:
                r = m - 1
            elif target > searchRow[m]:
                l = m + 1
            else:
                return True

        return False
