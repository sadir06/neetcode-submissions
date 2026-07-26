class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        solution = 0
        for num in nums:
            solution ^= num
        return solution
