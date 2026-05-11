class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = len(nums) - k
        for i in range(len(nums)):
            if i == j:
                return nums[i]