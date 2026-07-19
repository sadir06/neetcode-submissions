class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        overall_sum = sum(nums) # This is O(n)
        if overall_sum % 2 != 0: # Base case
            return False # Odd number, cannot be split evenly into 2 (we only have positive integets, cannot sum to a decimal)
        dp = {0}
        target = overall_sum // 2
        for num in nums:
            next_dp = set()
            for sums in dp: # This works because ???
                next_dp.add(sums + num)
            dp.update(next_dp) # Replaces dp with next_dp
            if target in dp:
                return True
        return False
