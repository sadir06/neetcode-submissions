from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return

        nums[:] = nums[-k:] + nums[:-k] # Take the last k values, and then attach them to the end, and take all the values until the last k values and then attach them on. If k is larger than the list, that just means that those extra k iterations will be wasted on just doing a circular loop and ending back up where you started. 
        