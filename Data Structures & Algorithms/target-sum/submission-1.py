class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, current_sum):
            if i == len(nums):
                if current_sum == target: # once all the numbers have been processed, we check if we have hit the target, and we return 1, else we return 0
                    
                    return 1
                else:
                    return 0
            if (i, current_sum) in dp:
                return dp[(i, current_sum)]
            scout_1 = dfs(i + 1, current_sum + nums[i])
            scout_2 = dfs(i + 1, current_sum - nums[i])


            dp[(i, current_sum)] = scout_1 + scout_2
            return dp[(i, current_sum)]
        
        return dfs(0, 0)