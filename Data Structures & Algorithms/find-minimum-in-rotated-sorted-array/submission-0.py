class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = min(nums), max(nums)

        return l