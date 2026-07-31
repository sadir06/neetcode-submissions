class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        while j < len(nums):
            i = j
            while i - 1 >= 0 and nums[i - 1] == nums[j]:
                nums.remove(nums[j]) # removes the first instance of it in the list
                i -= 1
                j -= 1
            j += 1
        return len(nums)