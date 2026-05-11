class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i, buy in enumerate(prices):
            if buy == max(prices):
                continue
            for j, sell in enumerate(prices):
                if j <= i:
                    continue
                maxP = max(maxP, sell - buy)

        return maxP