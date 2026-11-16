class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Given 2 positive integer arrays of length n and m respectively. We also have an integer success, and a combintation of spell and ption is considered successful if the profuct of their stringts is atleast success. Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell. Well what you could do is O(n * m) where you multiply every spell against every poition, check if it equals success and add to a counter that you eventually add to a results array of length spells. However since potions is always sorted in asending order, we can do binary search to see if each of the positions would be valid and move along that way and that improves it to O(nlogn). Doing this on the first example we can see that 5 * 3 = 15 > 7, so we go down the list to 2, and then 1, and then we find the final index that works and then do counter += len(potions) - left. There we go, it works!
        """
        output = []
        potions.sort() # Still O(nlogn)
        for spell in spells:
            left, right = 0, len(potions) - 1
            if potions[-1] * spell < success:
                output.append(0)
                continue
            while left < right:
                mid = left + ((right - left) // 2)
                strength = potions[mid] * spell
                if strength >= success:
                    right = mid # This might be the final correct value
                else:
                    left = mid + 1 # this value doesn't work
            output.append(len(potions) - right)
        return output
