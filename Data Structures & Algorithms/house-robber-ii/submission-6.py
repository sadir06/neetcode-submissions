class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def rob1(houses):
            n = len(houses)
            if n == 0:
                return 0
            if n == 1:
                return houses[0]
            dp = [0] * n
            dp[0], dp[1] = houses[0], max(houses[0], houses[1]) # The first house only makes as much money as it has, and the 2nd one chooses: do I rob the previous house and skip this one, or do I just take this one
            for i in range(2, n):
                dp[i] = max(dp[i - 2] + houses[i], dp[i - 1]) # We can either skip this house and take the previous sum, or take this new sum
                
            return dp[n - 1] # Same as dp[-1]
        return max(rob1(nums[:-1]), rob1(nums[1:]))