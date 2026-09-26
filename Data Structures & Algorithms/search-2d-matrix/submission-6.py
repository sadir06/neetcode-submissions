class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = (m * n) - 1

        # row = mid // n
        # col = mid % n 
        # This works because mid // n gives you for example 10 // 4 = 2, so you are in the 2nd row
        # And 10 % 3 = 1, in the first column. This always works, so use this trick

        while left <= right:
            mid = (left + right) // 2
            row, col = (mid // n), (mid % n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
            
        