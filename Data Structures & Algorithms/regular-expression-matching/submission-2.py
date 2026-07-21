class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            if j == len(p): # We have reached the end of the first word
                return True if i == len(s) else False # We only return True if both have reached the end at the same time, they are both correct
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            match = (i < len(s) and (s[i] == p[j] or p[j] == "."))
            result = False
            if j + 1 < len(p) and p[j + 1] == "*":
                if dfs(i, j + 2):
                    result = True
                elif match and dfs(i + 1, j):
                    result = True
            else:
                if match and dfs(i + 1, j + 1):
                    result = True



            dp[(i, j)] = result
            return result

        return dfs(0, 0)