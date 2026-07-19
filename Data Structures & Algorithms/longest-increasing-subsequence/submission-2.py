class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n # Initialising with ones makes our life a lot easier
        # What are our base cases here?
        if not nums:
            return 0
        if n == 1:
            return n

        for i in range(1, n):
            for j in range(i): # check every previous value
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j]) # This will also add the values of previous contiguous subsequences
        
        return max(dp)