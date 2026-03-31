class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l1 = 0 
        r1 = len(matrix) - 1
        row = None 

        while l1 <= r1:
            mid = l1 + ((r1 - l1) // 2)

            if matrix[mid][0] > target:
                r1 = mid - 1
            elif matrix[mid][-1] < target:
                l1 = mid + 1
            else:
                row = matrix[mid]
                break

        if not row:
            return False 
   
        l2 = 0
        r2 = len(row) - 1

        while l2 <= r2:
            mid = l2 + ((r2 - l2) // 2)

            if row[mid] > target:
                r2 = mid - 1
            elif row[mid] < target:
                l2 = mid + 1
            else:
                return True

        return False