class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
            if len(cost) == 1: # Base case
                return cost[0] 
            elif len(cost) == 0: # Just base cases covered here as we will consider 2 or more cases
                return 0
            cost.append(0) # Hidden top step
            dp = [0] * len(cost)
            # So the dp[i] is the total cheapest cost that you have to play to step on that floor
            dp[0], dp[1] = cost[0], cost[1] # It costs ateast those 2 amounts to step on either the 1st or the 2nd floor
            for i in range(2, len(cost)):
                dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i]) # The total cost to get to the current step is either you take one step from the previous one, or 2 steps from the 2nd most previous one and combine that with the cost of the current step

            return dp[-1] # We return the minimum cost to reach the top of the staircase, meaning that we return the top of our dp stack