class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)] # 2D array of 0s, where each dp[i][j] will represent the number of ways to get to that square
        # Only one way to get to the top row and left column, going right or down
        if ROWS == 1 and COLS == 1:
            return 1
        
        for i in range (COLS):
            dp[0][i] = 1

        for j in range(ROWS):
            dp[j][0] = 1
    
        for i in range(1, ROWS):
            for j in range(1, COLS):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] # Number of ways to reach the current square is the sum of everything from the top or the left

        return dp[ROWS - 1][COLS - 1]