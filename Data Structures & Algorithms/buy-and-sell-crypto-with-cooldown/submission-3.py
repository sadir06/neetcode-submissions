class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                # Here we do NOT buy
                dont_buy = dfs(i + 1, True) 
                dp[(i, buying)] = max(buy, dont_buy)
            else:
                sell = dfs(i + 2, True) + prices[i] # we skip a day, we can't buy or sell tomorrow, it's useless
                not_selling = dfs(i + 1, False)
                dp[(i, buying)] = max(sell, not_selling)

            return dp[(i, buying)]

        return dfs(0, True)
            