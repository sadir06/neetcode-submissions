class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]

        while l <= r:
            mid = (l + r) // 2 # Don't need to worry about indexing here, as we use the floor function
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            m = (l + r) // 2
            result = min(result, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1 # This means that we are in a sorted order, and we should move left up
            else:
                r = m - 1
            
        return result