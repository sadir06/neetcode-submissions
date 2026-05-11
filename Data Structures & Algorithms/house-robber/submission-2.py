class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n # where dp[n - 1] is the maximum money that can be made

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp[0] = nums[0] # Minimum length of 1
        
        for i in range(n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])



        return dp[n - 1]