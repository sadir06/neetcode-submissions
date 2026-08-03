class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_bound = max(weights) # O(n)
        max_bound = sum(weights) # O(n)
        total = sum(weights)
        while min_bound < max_bound: # < because they could eventually be the same value and we don't want an infinite loop
            mid = min_bound + (max_bound - min_bound) // 2
            total_weight = 0
            j = 0
            for i in range(days): # O(days * n) 
                cur_weight = 0
                while j < len(weights):
                    if cur_weight + weights[j] > mid:
                        break
                    cur_weight += weights[j] # Add on the weights until we can't anymore
                    j += 1 # Keep moving along the weights
                total_weight += cur_weight # check how much weight has been collected 
            if total_weight == total:
                max_bound = mid # This is a valid mid bound
            else:
                min_bound = mid + 1 # Mid is not valid we need to skip it


        return min_bound 