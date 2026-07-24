class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_queries = sorted(enumerate(queries), key=lambda x:x[1])
        intervals.sort(key=lambda x:x[0]) # Sort by start times
        min_heap = []
        output = [-1] * len(queries)
        i = 0
        for index, query_val in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query_val:
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while min_heap and min_heap[0][1] < query_val:
                heapq.heappop(min_heap)
            else:
                if min_heap:
                    output[index] = (min_heap[0][0])

        return output