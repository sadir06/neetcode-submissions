class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_val = float('inf')
        for num in nums:
            min_val = min(num, min_val)

        return min_val