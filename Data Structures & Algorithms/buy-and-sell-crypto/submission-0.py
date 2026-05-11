class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute Force method

        max_val = 0
        for i, num in enumerate(prices):
            for j, num2 in enumerate(prices):
                if j <= i:
                    continue
                curVal = num2 - num
                if curVal > max_val:
                    max_val = curVal
        return max_val