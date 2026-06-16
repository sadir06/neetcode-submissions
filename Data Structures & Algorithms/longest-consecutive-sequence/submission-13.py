class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # Remember we don't have to build the list, but just find the longest consecutive sequence
        mp = defaultdict(int)
        res  = 0
        for num in nums:
            if not mp[num]:
                length = mp[num - 1] + mp[num + 1] + 1 # +1 for itself
                mp[num] = length # Length for the current sequence
                mp[num - mp[num - 1]] = length
                mp[num + mp[num + 1]] = length

                res = max(res, mp[num])

        return res