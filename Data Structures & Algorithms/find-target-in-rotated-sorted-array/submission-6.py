class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right, run = 0, len(nums) - 1, ""

        while left <= right: # We can check if we are in the upper / lower bound, and use that to find the target
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid 
            if nums[left] <= nums[mid]: # The left half is fully sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # The right half is FULLY sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1 # We haven't found anything