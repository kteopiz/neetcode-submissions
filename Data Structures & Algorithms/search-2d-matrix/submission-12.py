class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows - 1
        arr = None
        while l <= r:
            mid = (l + r) // 2
            print('mid' ,mid)
            print('m', matrix[mid])
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][cols - 1]:
                l = mid + 1
            else:
                arr = matrix[mid]
                break
        
        if not arr:
            return False
        print('arr', arr)
        
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if target < arr[mid]:
                r = mid - 1
            elif target > arr[mid]:
                l = mid + 1
            else:
                return True

        return False
        