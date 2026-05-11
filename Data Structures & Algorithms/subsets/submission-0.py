class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy()) # Creates a shallow copy of the list, this is the very last case, where we juts add a the final list onto the result set
                return # We end it
            subset.append(nums[i]) # Append the singular version of the subset, e.g. [1], [2]

            dfs(i + 1) # Loop for all

            subset.pop()

            dfs(i + 1)

        dfs(0)
        return result