class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            lookup = target - num
            if lookup in seen:
                return [seen[lookup], i]
            seen[num] = i # Set it to the current index, so that we return the right index
