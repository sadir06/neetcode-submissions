class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_positive = 1 # It can only be 1
        positive_so_far = 0
        nums.sort()
        for num in nums:
            if num <= 0:
                continue
            if num == positive_so_far:
                continue # It's just the same number repeated
            if num == positive_so_far + 1:
                positive_so_far = num
            elif num == positive_so_far + 2:
                return positive_so_far + 1
        min_positive = max(positive_so_far + 1, min_positive)
        return min_positive
            