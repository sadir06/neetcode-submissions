class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right: # Not less than equal to BECAUSE specifically here the same number can't sum to the target, that just doesn't make sense. 
            lnum = numbers[left]
            rnum = numbers[right]
            if rnum + lnum == target:
                return [left + 1, right + 1] # List indexing starts at 0 in python, they want 1-indexed not 0-indexed. 
            elif rnum + lnum >= target: # Asending order, if it is greater than target or equal, it cannot SUM to target, go to the next index
                right -= 1
            elif rnum + lnum < target: # If rnum is less than target, but lnum + rnum is smaller than target, lnum is too small, increment
                left += 1
        return "You are a dumbass" # Self Explanatory

