class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1 # Left and right
        while l <= r:
            mid = l + (r - l) // 2 # Floor function

            row , col = mid // cols, mid % cols # mid divided by the colum length is the new row, and mid / col remainder is the new column
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        return False