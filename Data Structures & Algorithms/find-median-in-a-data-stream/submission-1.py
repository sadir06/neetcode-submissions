class MedianFinder:
    # Ok so in this quesiton we have to implement a median finder class. This initialises the object, and adds an integer form the data stream to the data structure. Then, we return the median of all the elements so far

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None: # O(logn) -> Because heap push operations are logn because it's a tree
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
        elif num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num) # Store the smaller half of hte numbers in the max heap
        else:
            heapq.heappush(self.min_heap, num) # Store the larger half in the min heap 

        if len(self.min_heap) > len(self.max_heap) + 1:
            moved_val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -moved_val)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            moved_val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, moved_val)
    def findMedian(self) -> float:
        if not self.max_heap:
            return 0.0
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
        
        