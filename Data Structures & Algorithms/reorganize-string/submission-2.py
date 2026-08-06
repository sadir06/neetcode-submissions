from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(max_heap)
        prev = None
        result = ""
        while max_heap or prev:
            if prev and not max_heap: # We have run out of letters, but there's still a previous value (meaning that the frequency of it DID NOT drop to 0) and we still have a couple of letters to put in, but the max heap ran out of space
                return ""

            cnt, char = heapq.heappop(max_heap)
            result += char
            cnt += 1
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if cnt != 0: 
                prev = (cnt, char)

        return result