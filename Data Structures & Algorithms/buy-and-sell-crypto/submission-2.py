class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i, sell in enumerate(prices):
            for j, buy in enumerate(prices):
                if j <= i:
                    continue
                maxP = max(maxP, buy - sell)

        return maxP