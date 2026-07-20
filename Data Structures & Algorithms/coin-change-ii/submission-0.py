class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {} # Dict-> (index, remaining_amount) : num of valid combinations found from that state

        def dfs(i, remaining):
            if i == len(coins) or remaining < 0:
                return 0
            if remaining == 0:
                return 1
            
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            total_paths = dfs(i, remaining - coins[i]) # this is our new current, but we can pick the same coin again
            total_paths += dfs(i + 1, remaining) # this prevents counting 1 + 2 and 2 + 1 as difference combinations, as if we skip 1, we never go back!
            dp[(i, remaining)] = total_paths

            return dp[(i, remaining)]

        return dfs(0, amount)