class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * n
        dp[0], dp[1] = 1, 2 # There is 1 way to climb up 1 stair and 2 ways to climb up 2. 
        # dp[i] represents the number of ways you can climb i + 1 stairs. Simpe as that
        # dp[i] always will equal 1 + dp[i - 1], simple as that

        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1] # We return the final one as that will hold the final answer