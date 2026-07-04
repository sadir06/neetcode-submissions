class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # Remember we don't have to build the list, but just find the longest consecutive sequence
        
        map = set(nums)
        longest = float("-inf") # We will have atleast a sequence of length 1
        for num in nums:
            current = 1
            i = num
            while i + 1 in map: # this is O(1), the check, so it's all good
                current += 1
                i += 1 
            longest = max(longest, current)

        return longest if longest != float("-inf") else 0