from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        We are given an integer array nums and an integer k. The frequency of an element x is the number of times it occurs in an array. An array is good if the frequency of all elements is less than or equal to k. Return the length of the longest good subarray of nums. We we could just go through and count all subarrays and check their frequencies, but ther eis a better way. Since we are lokoing for a subarray, we can take a sldingin winodw approach, returning max (max, right - left + 1) at the end, recording the max length as we go. We can define left from 0, and do a loop for the right, looping through the array, and we have a dictionary that keeps counts of the different elements in our current window. We will have the largest of those, and then we keep moving the subarray, and a valid one is when the max frequency is k or less. Then we record the length and keep going. 
        """
        left = 0
        frequencies = defaultdict(int)
        max_length = 0
        for right in range(len(nums)):
            frequencies[nums[right]] += 1
            max_frequency = frequencies[nums[right]]
            while left <= right and max_frequency > k:
                frequencies[nums[left]] -= 1
                left += 1
                max_frequency = frequencies[nums[right]]
            if max_frequency <= k:
                max_length = max(max_length, right - left + 1)
            
        return max_length
