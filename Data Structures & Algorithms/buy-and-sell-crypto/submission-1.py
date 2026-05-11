class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Sliding Window Method
        l, r = 0, 1
        maxVal = 0

        while r < len(prices): #Don't let the sliding window go out of range
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxVal = max(maxVal, profit) # This is just another way of doing the if condition
            else:
                l = r
            r += 1 # The right window is always increaasing, so it is a growing window. If the prices of right are greater, then keep checking the window for the best prices. As soon as the left side is greater (i.e. profit is negative) move onto the same value as r
        return maxVal