class Solution:
    def climbStairs(self, n: int) -> int:
        #Recursive Implementation
        def dfs(i): 
            if i >= n: # If i is equal to n, return True
                return i == n
            return dfs(i + 1) + dfs(i + 2) # Find the recursive sum of i + 1 + i + 2 (all the combinations of adding 1 and 2, without it equalling n)
        return dfs(0) # Return it from i = 0, as that is out starting point