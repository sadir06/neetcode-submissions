class LFUCache:

    def __init__(self, capacity: int):
        self.space = capacity
        self.store = {}

    def get(self, key: int) -> int:
        if key in self.store:
            self.store[key][1] += 1
            return self.store[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.space == 0:
            LFU = [0, float("inf")]
            for keys, values in self.store.items():
                val, freq = values
                if freq < LFU[1]:
                    LFU = [keys, freq]

            del self.store[LFU[0]] # Delete the least recently used key
            self.space += 1
        if key in self.store:
            count = 1 + self.store[key][1]
            self.store[key] = [value, count]
        else:
            self.store[key] = [value, 0]
            self.space -= 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)