class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}


        def dfs(i, j):
            if j == len(t):
                return 1 # We have a valid paht

            if i == len(s):
                # j has not finished yet, but we ran out of letters in the source string. 0 valid patterns found
                return 0

            if (i, j) in dp:
                return dp[(i, j)]
            
            if s[i] != t[j]:
               total_ways = dfs(i + 1, j) # Current letter doesn't match, so try the next letter with the current letter of t
            else: # We have a match!
                total_ways = dfs(i + 1, j + 1) + dfs(i + 1, j)
            
            dp[(i,j)] = total_ways

            return dp[(i,j)]
        
        return dfs(0, 0)
                