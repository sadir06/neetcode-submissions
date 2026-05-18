class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # Remember we don't have to build the list, but just find the longest consecutive sequence
        if not nums:
            return 0

        result = 0
        nums.sort() # Sorts in place, returns None
        curr, streak = nums[0], 0
        i = 0

        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and curr == nums[i]:
                i += 1
            curr += 1
            streak += 1
            result = max(result, streak)
        return result
