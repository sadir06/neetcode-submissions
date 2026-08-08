class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        store = set(dictionary)
        dp = {len(s) : 0}

        def dfs(i):
            if i in dp:
                return dp[i]    
        # Try both options of treating each value as an extra character, vs trying to match it to a word in store, and take the min value of the 2, as self.result is taking all characters from this point as not a word vs checking for words, and we take the min value of that, where dfs(j + 1) will only be higher if we never hit if word in store. 
            self.result = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                word = s[i:j + 1]
                if word in store:
                    self.result = min(self.result, dfs(j + 1))
            dp[i] = self.result
            return self.result



        dfs(0)
        return self.result 