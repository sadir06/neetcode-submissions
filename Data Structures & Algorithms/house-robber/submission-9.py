class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base cases -> We need a lot bruh
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1]) # The first house only makes as much money as it has, and the 2nd one chooses: do I rob the previous house and skip this one, or do I just take this one
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]) # We can either skip this house and take the previous sum, or take this new sum
            
        return dp[n - 1] # Same as dp[-1]