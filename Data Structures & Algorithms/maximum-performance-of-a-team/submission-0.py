import heapq as hq

class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        pairs = list(zip(efficiency, speed))
        pairs.sort(key=lambda x : x[0], reverse=True)
        min_heap = []
        max_performance = float("-inf")
        carried_sum = 0
        for curr_efficiency, curr_speed in pairs:
            hq.heappush(min_heap, curr_speed)
            carried_sum += curr_speed
            while len(min_heap) > k:
                val = hq.heappop(min_heap)
                carried_sum -= val
            
            max_performance = max(max_performance, carried_sum * curr_efficiency)

        return max_performance % (10 ** 9 + 7)