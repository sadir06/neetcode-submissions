import heapq as hq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t : t[0])
        res, min_heap = [], []
        i, time = 0, tasks[0][0]

        while min_heap or i < len(tasks): # While we still have tasks to go
            while i < len(tasks) and time >= tasks[i][0]: # While it is ready to be enqueued
                hq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not min_heap:
                time = tasks[i][0]
            else:
                processing_time, index = hq.heappop(min_heap) # We always select the smallest
                time += processing_time # We will wait for this process to be completed
                res.append(index) # this is the one htat we will process

        return res