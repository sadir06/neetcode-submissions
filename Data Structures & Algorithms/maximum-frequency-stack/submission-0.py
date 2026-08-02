import heapq as hq
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.heap = []
        self.cnt = defaultdict(int) # initialises every key with an int value
        self.index = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        hq.heappush(self.heap, (-self.cnt[val], -self.index, val))
        self.index += 1

    def pop(self) -> int:
        _, _, val = hq.heappop(self.heap) # This is a max heap, so it first sorts by the largest count of a number, nad then the actual index that it is in. This is why this works at popping the correct value, the most frequent one that is closest to the top.  
        self.cnt[val] -= 1 
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()