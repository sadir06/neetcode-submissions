class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """
        Given an array of integer nums, calculate the pivot index of this array. The pivot index is the index where the sum of all the mubers to the left of the index is equal to the sum of all the numebrs to the right. Return the leftmost index that is a pivot index. If none exists, return -1. IF the index is on th eleft edge, the left sum is 0, because there are no elemnets to the left. Essentially, we can just do a prefix sum solution, where we do one array that contains left hand side sums, and the other has right hand sums, we compare the 2 arrays elementwise and see if any of them equal, and since we do left to right comparison, we just return as soon as we find a match, else we return -1. Simple. 
        """
        n = len(nums)
        left, right = [0] * n, [0] * n
        for i in range(1, len(nums)):
            left[i] = nums[i - 1] + left[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i + 1] + right[i + 1]
        print(left, right)
        for i in range(len(nums)):
            if left[i] == right[i]:
                return i
        return -1