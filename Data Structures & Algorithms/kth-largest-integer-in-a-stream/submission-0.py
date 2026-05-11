class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # use heapq.heapify() to turn a given list into a min heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # Remove terms until we reach the kth largest term ()

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]  
