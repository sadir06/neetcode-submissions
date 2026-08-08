class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Given an integer array nums, and an integer k, return True if possible to dicide this araray into k non-empty subsets whose sums are all equal. So the target sum is sum(nums) // k
        if sum(nums) % k != 0:
            return False # We need to have an integer sum
        subset_sum = sum(nums) / k # Each subset needs to sum to this

        sums = [0] * k # Each value represents the current sum of the k subsets

        def dfs(i):
            if i == len(nums): # We have reached the end without any problems, so return True
                return True

            for j in range(len(sums)): # Try adding the value to each of the different values and check if the sums workout
                if sums[j] + nums[i] <= subset_sum:
                    sums[j] += nums[i]
                    if dfs(i + 1):
                        return True # This means we have passed the checks and the subset sums are equal
                    sums[j] -= nums[i]

                    if sums[j] == 0:
                        break

            return False
            
        return dfs(0)


        
