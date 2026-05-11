class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lowest_buy = prices[0]
        for sell in prices:
            maxP = max(maxP, sell - lowest_buy)
            lowest_buy = min(lowest_buy, sell)

        return maxP