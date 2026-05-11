class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) 
        for i, num in enumerate(nums):
            mid = ((left + right)//2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
                continue
            elif nums[mid] < target:
                left = mid
                continue
        return -1