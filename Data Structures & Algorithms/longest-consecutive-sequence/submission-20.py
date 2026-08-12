class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        My code was already here, so I muyst have done this quesiotn already, and I think I remember what to do, we can use a hash set to find starting numbers, and go from there. Nonetheless let's do it. Given an unsorted array of integers nums, return the length (ok so we return an int) of the longest consecituve elements sequence. OK so we have to do this without sorting, else it would be incredibly easy, just sort it, and start counting with consecutive sequences and then store a max length value vs a cur length value and update as you go. 
        However, O(n) is also relatively trivial, use a hashset for O(1)) lookup (duplicates don't matter here because we can just find consectutive elements ignoring duplicates), and for each element, it is either the start of an element or just part of a sequence. For each value in nums, we do a search if i - 1 is in the set, if yes we move on, else we know it is the starter and we start counting from there. 
        """
        maxLen = 0
        mySet = set(nums)
        for num in mySet: # Stops you from iterating through a bunch of duplicate numbers that don't matter anyway, and redoing work again and again. 
            curLen = 0
            if (num - 1) in mySet:
                continue # This is part of a sequence, like the 2 in 1, 2, 3, 4
            else: # This is the start of a sequence like the 1 in 1, 2, 3, 4   
                cur_val = num
                curLen += 1 
                while (cur_val + 1) in mySet: # O(1)
                    curLen += 1 # While the current number + 1 is in the set, add it to our sequence, increase the lenght, and try the next value
                    cur_val += 1
            maxLen = max(maxLen, curLen)

        return maxLen