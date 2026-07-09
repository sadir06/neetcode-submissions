class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap) # create a min heap so that we can find the k closest points. 

        for point in points:
            x, y = point
            heapq.heappush(heap, (-((x) ** 2 + (y) ** 2), point))
            if len(heap) > k:
                heapq.heappop(heap)
        min_heap = [point for dist, point in heap]

        return min_heap