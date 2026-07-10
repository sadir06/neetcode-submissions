class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # nums ins a min heap now

        while len(nums) > k:
            heapq.heappop(nums) # While the length of nums is nums are greater than k, pop the n - k smallest values, so we wil have exactly k values left
        
        return nums[0] # We return the value at the top which will be the kth largest element in the heap

