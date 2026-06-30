class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Firstly, h is always atleast equal to the size of the array or larger than it. 
        # Given this, the upper bound for the answer is x / k hours, rounded up: use ceil(x / k) = t of h
        # This means that the sum of ceil(all(x) / k) = h 
        # The upper bound for k is simply the largest given value in the list: max(piles)
        # m is the largest in the pile, and there are n numbers of piles
        # We could just search every value from 1 to m (this could be absolutely massive) to find the minimum value at which Koko can finish the task
        # The smarter way is to just binary search it, and jump from 1 -> m in leaps
        m, n = max(piles), len(piles) # O(n)
        left, right = 1, m # We will create our mid using these 2 values
        while left < right: 
            mid = (left + right) // 2 # Or we could use left + (right - left) // 2 -> Safer for larger memory
            hours_needed = 0 # Set this to 0 in each iteration
            for i in range(n): # O(n * logm) -> This iteration happens log m times because of binary search and we have n iterations each time
                hours_needed += math.ceil(piles[i] / mid)
            if hours_needed <= h: 
                right = mid
            else:
                left = mid + 1
        return left
