import copy
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = copy.deepcopy(nums)
        return nums + nums2