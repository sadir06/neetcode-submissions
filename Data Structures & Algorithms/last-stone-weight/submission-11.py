class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap) # Create a max heap of stones. 
        if len(heap) == 1:
            return -heap[0]
        while len(heap) > 1:
            stone1, stone2 = -heapq.heappop(heap), -heapq.heappop(heap)
            if stone1 > stone2:
                heapq.heappush(heap, -(stone1 - stone2))
            else:
                continue
        
        return -heap[0] if len(heap) == 1 else 0