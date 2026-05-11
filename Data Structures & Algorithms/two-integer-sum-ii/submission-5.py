class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # This is the 2 pointers algorithm
        l, r = 0, len(numbers) - 1

        while l < r:
            current_sum = numbers[r] + numbers[l]
            if current_sum == target:
                return [l + 1, r + 1] # We have to add + 1 because we are returning the indexes as if they start at 1 instead of 0. 
            elif current_sum > target: # We can do these two comparisons because we know that the list is arranged in increasing order - therefore, decreasing r will decrease the current sum, and increasing l will increase the current sum.
                r -= 1
            else:
                l += 1
        return []