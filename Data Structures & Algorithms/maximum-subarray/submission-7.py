class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)): # For greedy we only go through the array one time
            current_sum = max(current_sum + nums[i], nums[i]) # Current sum can be negative
            max_sum = max(max_sum, current_sum)
        return max_sum