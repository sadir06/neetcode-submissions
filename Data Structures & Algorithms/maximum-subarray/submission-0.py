class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)] # Create an n x 2 maxtrix, dp[i][1] = max subarray sum that must start at index i (that we are iterating for), dp[i][0] = maximum subarray sum that starts at index i or later
        dp[n - 1][1] = dp[n - 1][0] = nums[n - 1] # Initialise the base cases at the last index (they must be equal to nums[n - 1] as that is the last term)

        for i in range(n - 2, -1, -1): # Iterate backwards from n - 2 down to 0
            dp[i][1] = max(nums[i], nums[i] + dp[i + 1][1]) # Compute this term, and either start a new subarray, using nums[i], or extend the subarray by using nums[i] + dp[i + 1][1]
            dp[i][0] = max(dp[i + 1][0], dp[i][1]) # Compute this term, where the best subarra either starts later, or exactly at i.

        return dp[0][0] # Return the first term, as we built the dp table backwards. 
        