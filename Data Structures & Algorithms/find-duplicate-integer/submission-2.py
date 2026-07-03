class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}

        for i, num in enumerate(nums):
            if num in map:
                return num
            else:
                map[num] = 1 + map.get(num, 0) 