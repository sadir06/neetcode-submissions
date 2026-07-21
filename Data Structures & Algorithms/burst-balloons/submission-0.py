class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1] # We pad the array so that we don't have to worry about going out of bounds when multiplying
        dp = {}

        def dfs(left, right):
            max_score = 0
            if (left, right) in dp:
                return dp[(left, right)]
            for i in range(left + 1, right):
                score = dfs(left, i) + dfs(i, right) + (nums[left] * nums[right] * nums[i]) # These are the final balloons that will be there
                max_score = max(score, max_score)

            dp[(left, right)] = max_score
            return dp[(left, right)]

        return dfs(0, len(nums) - 1)