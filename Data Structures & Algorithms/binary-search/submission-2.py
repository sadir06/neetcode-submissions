class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1  # Note: -1 because indices are 0-based
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                # Target is in the left half, move right boundary
                right = mid - 1
            
            else:
                # Target is in the right half, move left boundary
                left = mid + 1
                
        return -1