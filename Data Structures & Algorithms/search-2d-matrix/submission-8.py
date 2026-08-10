class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (r + l) // 2
            row = matrix[mid]
            if target < row[0]:
                r = mid - 1
            elif target > row[len(row) - 1]:
                l = mid + 1
            else:
                # we are in the row that would house the target value
                break
        else:
            return False
        
        searchRow = matrix[(l + r) // 2]
        
        l, r = 0, len(searchRow) - 1
        
        while l <= r:
            mid = (r + l) // 2
            if target < searchRow[mid]:
                r = mid - 1 
            elif target > searchRow[mid]:
                l = mid + 1
            else:
                return True
        return False