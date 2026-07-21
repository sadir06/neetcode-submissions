class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2): # We have reached the end!
                return len(word1) - i 
            
            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                operations = dfs(i + 1, j + 1) # We have the same letter move both
            else:
                operations1 = 1 + dfs(i + 1, j + 1)
                operations2 = 1 + dfs(i + 1, j)
                operations3 = 1 + dfs(i, j + 1)
                operations = min(operations1, operations2, operations3)


            dp[(i, j)] = operations

            return dp[(i, j)]

        return dfs(0, 0)