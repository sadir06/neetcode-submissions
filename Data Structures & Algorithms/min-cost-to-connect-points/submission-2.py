class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((distance, j)) 
                adj[j].append((distance, i)) 

        visited = set()
        min_heap = []
        total_cost = 0
        heapq.heappush(min_heap, (0, 0))
        
        while min_heap:
            cost, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue
            visited.add(current_node)
            total_cost += cost
            if len(visited) == n:
                return total_cost

            for node in adj[current_node]:
                if node[1] not in visited:
                    heapq.heappush(min_heap, (node[0], node[1]))
