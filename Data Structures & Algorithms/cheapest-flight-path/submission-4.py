class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0 # Set the price of the starting city to 0, obviously
        for _ in range(k + 1):
            tmpPrices = prices.copy()
            for source, dest, cost in flights:
                if prices[source] == float("inf"):
                    continue
                if prices[source] + cost < tmpPrices[dest]:
                    tmpPrices[dest] = prices[source] + cost 
            prices = tmpPrices

        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]