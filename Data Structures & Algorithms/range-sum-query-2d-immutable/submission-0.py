class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.grid = matrix # List of lists of integers, this is our grid that we'll be working with

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Given a range of rows and cols, we will find the sum of all the values form the grid in the given regions
        ROWS, COLS = len(self.grid), len(self.grid[0]) # Our out of bounds parameters
        region_sum = 0
        for r in range(row1, row2 + 1):
            for c in range (col1, col2 + 1):
                region_sum += self.grid[r][c]

        return region_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)