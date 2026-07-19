class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for num in nums:
            temp = curMax * num
            curMax = max(num, num * curMax, num * curMin) # This picks the maximum of either starting a new subarray, extending the previous max, or the negative flip case (where a really small negative value multiplied by a really small negative number can blow up into massive positive values)
            curMin = min(num, temp, num * curMin) # The min is either the current value, the previous max, or the continued min window
            res = max(res, curMax)

        return res