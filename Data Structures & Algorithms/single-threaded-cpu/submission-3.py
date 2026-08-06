import heapq as hq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Preserve the original index
        for i, task in enumerate(tasks):
            task.append(i) # this is a nice trick to preserve the original ordering
        
        tasks.sort(key=lambda t : t[0]) # Sort by enqueue times
        res, min_heap = [], []
        i, time = 0, tasks[0][0] # take the first task with the smallest enqueue time
        while min_heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                hq.heappush(min_heap, [tasks[i][1], tasks[i][2]]) # Append the index and the processing time
                i += 1

            if not min_heap:
                time = tasks[i][0]
            else:
                procTime, index = hq.heappop(min_heap)
                time += procTime
                res.append(index)

        return res