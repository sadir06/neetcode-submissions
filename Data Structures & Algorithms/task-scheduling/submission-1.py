class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        queue = collections.deque()
        time = 0

        while max_heap or queue:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    queue.append((cnt, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time


