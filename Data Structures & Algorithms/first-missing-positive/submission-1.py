class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                i += 1
                continue # because we cannot insert these in the correct places in the list

            index = nums[i] - 1 # 0-indexed
            if nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
            else:
                i += 1
        for i in range(n): # i starts again from 0
            if nums[i] != i + 1:
                return i + 1 # We have found the missing term, it's somewhere in the middle
        return n + 1 # The smallest missing consecutive positive integer is JUST outside the list