class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1

        while l != r:
            mid = (r + l) // 2
            row = matrix[mid]
            print(l,r,mid)
            if target < row[0]:
                # matrix = matrix[0:mid]
                r = mid
            elif target > row[len(row) - 1]:
                # matrix = matrix[mid + 1:len(matrix)]
                l = mid + 1
            else:
                l = mid
                break
        
        searchRow = matrix[l]
        
        # print(searchRow)

        l, r = 0, len(searchRow) - 1
        
        while l <= r:
            mid = (r + l) // 2
            # print(l,r,mid)
            if target < searchRow[mid]:
                r = mid - 1 
            elif target > searchRow[mid]:
                l = mid + 1
            else:
                return True
        return False