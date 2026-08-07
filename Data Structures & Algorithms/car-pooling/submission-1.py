class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1]) # Sort by start times

        min_heap = []
        curPass = 0

        for numPass, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                curPass -= heapq.heappop(min_heap)[1]

            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(min_heap, [end, numPass])

        return True 