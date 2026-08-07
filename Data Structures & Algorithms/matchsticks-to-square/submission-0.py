class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side_length = sum(matchsticks) / 4 # We need 1 matchstick on each side to make this possible
        if (sum(matchsticks) % 4) != 0:
            return False
        
        side = [0] * 4 # We will fill up the 4 buckets as the 4 sides, each needs to equal side_length
        matchsticks.sort(reverse=True)
        def dfs(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if matchsticks[i] + side[j] <= side_length:
                    side[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    side[j] -= matchsticks[i]
                    
                    if side[j] == 0:
                        break
            return False


        
        return dfs(0)