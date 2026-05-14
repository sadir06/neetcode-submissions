class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            subtract = target - num
            if subtract in hashmap:
                return [hashmap[subtract], i]
            else:
                hashmap[num] = i
        return []

