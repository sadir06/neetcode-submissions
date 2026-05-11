class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starting = set(nums)
        longest = 0


        for n in nums:
            if (n - 1) not in starting:
                length = 1 # At a new term, length will always be 1
                while (n + length) in starting:
                    length += 1
                longest = max(length, longest)

        
        
        return longest
