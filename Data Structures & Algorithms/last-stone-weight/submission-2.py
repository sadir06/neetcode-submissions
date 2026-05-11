class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # We want a maxHeap not a minHeap
        heapq.heapify(stones) # Create a heap of stones
        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)

            if x == y:
                continue
            if x < y:
                heapq.heappush(stones, x - y)
        stones.append(0)
        return abs(stones[0])