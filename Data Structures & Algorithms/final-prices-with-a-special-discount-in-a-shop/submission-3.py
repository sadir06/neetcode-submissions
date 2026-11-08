class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        We are given a list of prices, where for each item at index i, we have to find the first later item whose original price is less than or equal to the current price. Find the FIRST LATER item whose price is less than or equal to the current price. Then subtract that later price as a discount (curr - future_less_than_or_eq), and then return the final prices in the original order. Discounts are always determine from the input prices. OK this is immediately a monotonic stack question, where we are determining prices that are smaller, so we always go in descending order. Because if a price comes in the future that is larger, then we instantly know that we will never pick it to a price that is lower. So we have to do this: Loop through the list, create an output list and then for each element in prices, you have to find the future element that is the smallest future one. SO we do a one pass create this monotonic stack and then we create the output list. 
        """
        res = prices.copy()
        stack = []
        
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prev_idx = stack.pop()
                res[prev_idx] -= price
            stack.append(i)
        return res