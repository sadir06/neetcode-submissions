class StockSpanner:

    def __init__(self):
        self.store = []

    def next(self, price: int) -> int:
        self.store.append(price)
        span = 1
        for i in range(len(self.store) - 1):
            if price >= self.store[i]:
                span += 1
            else:
                span = 1
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)