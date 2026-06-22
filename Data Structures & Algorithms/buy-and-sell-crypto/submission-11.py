class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = prices[0] # Tracks the absolute cheapers price seen so far up to the current day
        maximum_profit = 0

        for price in prices:
            min_buy_price = min(price, min_buy_price)
            current_profit = price - min_buy_price
            maximum_profit = max(current_profit, maximum_profit)

        return maximum_profit

        