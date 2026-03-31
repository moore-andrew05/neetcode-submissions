class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u = 0
        d = len(matrix) - 1

        mid = 0

        while u <= d:
            mid = u + ((d - u) // 2)
            val_start = matrix[mid][0]
            val_end = matrix[mid][-1]

            if val_end < target:
                u = mid + 1

            elif val_start > target:
                d = mid - 1

            else:
                break

        row = matrix[mid]
        
        l = 0
        r = len(row) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            val = row[mid]

            if val > target:
                r = mid - 1

            elif val < target:
                l = mid + 1

            else:
                return True


        return False




















