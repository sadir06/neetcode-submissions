class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # Remember we don't have to build the list, but just find the longest consecutive sequence
        res = 0
        store = set(nums) # Turn the list into a set, O(1) lookup using the "in" keyword

        for num in nums: # O(n)
            streak, curr = 0, num # streak = current streak, curr = the current number
            while curr in store: # O(n), If the current value is in store
                streak += 1 # Increase streak by 1
                curr += 1 # Increase the current value by 1, and check if it is in the list -> We can do this with just the nums list as well, but using a set makes it faster. 


            res = max(res, streak) # max between oldest max result, and current longest streak


        return res