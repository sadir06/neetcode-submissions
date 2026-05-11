class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> list[int]:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]