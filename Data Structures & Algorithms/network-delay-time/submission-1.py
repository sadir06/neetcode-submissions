class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hashMap = defaultdict(list)

        for source, target, time in times:
            hashMap[source].append((target, time)) # This is the adjacecy list that given a source return sthe next target (directed) and the weight of the target, we append here because we want to append to the list, mutliple arrows could come from the same source
        min_heap = []
        heapq.heappush(min_heap, (0, k))
        visited = set()

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap) # Gives us the shortest time first

            if curr_node in visited:
                continue # skip this, we might have pushed a slower duplicate path to this node earlier, and we eliminate this because that's hoe Dijkstra's works. 
            visited.add(curr_node) # We have locked in the fastest time to reach this node

            if len(visited) == n:
                return curr_time # We have reached every single computer in the network since we have all nodes in the visited set, so our current time is the shortest amount of possible time to reach all nodes
            else:
                for node in hashMap[curr_node]: # Explore the neigbors
                    if node[0] not in visited:
                        heapq.heappush(min_heap, (curr_time + node[1], node[0]))
            
        return -1