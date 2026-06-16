class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # Remember we don't have to build the list, but just find the longest consecutive sequence
        if not nums:
            return 0
        
        store = set()
        starting = []
        longest_frequency = 0

        for num in nums:
            store.add(num)

        for num in nums:
            if num - 1 not in store:
                starting.append(num)

        for num in starting:
            current = 1
            while (num + 1) in store: # O(1)
                current += 1
                num += 1 
            longest_frequency = max(current, longest_frequency)
                
        return longest_frequency

        
