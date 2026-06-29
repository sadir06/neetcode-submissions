class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_val = float("inf")

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]: # This means we are still in the low run
                run = "low"
            else:
                run = "high"
            if run == "low":
                right = mid # keep mid, as it is part of the lower run and can still contain the lowest number
            else:
                left = mid + 1 # Mid is now part of the lowest run and can no longer contain the lowest number



        return nums[left]

