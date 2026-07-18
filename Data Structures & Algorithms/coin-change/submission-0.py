class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # dp[i] represents hte minimum number of coins to make amount i
        if not coins:
            return -1
        if not amount:
            return 0
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])



        return -1 if dp[-1] == amount + 1 else dp[-1]