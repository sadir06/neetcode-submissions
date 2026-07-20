class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        ROWS, COLS = len(text1), len(text2)
        
        dp = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)] # Initialise it with 0s, dp[i][j] represents the length of the longest common subsequence using a slice of text1 up to index i and a slice of text2 up to index j. 
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                if text1[i - 1] == text2[j - 1]: # We have found a match!
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[ROWS][COLS]