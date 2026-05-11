class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) # This is now a maxHeap

        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)

            if x == y:
                continue
            elif x < y:
                heapq.heappush(stones, x - y)
        
        if len(stones) == 0:
            return 0


        return abs(stones[0]) # This contains the maximum value
