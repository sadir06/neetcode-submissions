class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # Create a results list that we return that has all 1s
        # We will store out multiplicative sums here and return it in the end

        prefix = 1 # Set your initial prefix to 1, we will update it to be the multiplilcative sum of what we have so far
        for i in range(len(nums)): # Loop through each value in the given list
            res[i] = prefix # Set the result of i to the curernt prefix
            prefix *= nums[i] # Multiply every term by the next term, so that result becomes a list of all sums by each other (as in the given example, we get [1, 1, 2, 8])
            # Note that we are 1 step behind as we do the prefix multiplication AFTER setting the values in the results list. 
        postfix = 1 # Set a value that we will use for the reverse loop
        for i in range(len(nums) - 1, -1, -1): # Now we loop through again (O(n + n) = O(n)), however, in REVERSE, starting from len(nums) - 1 (because of list indexing starting at 0), and go back by 1 evry time until we reach the start of the list
            # In this list, we have to do the same thing, just multiply in reverse
            res[i] *= postfix # Make sure to multiply and not overwrite
            postfix *= nums[i] # results vector is again multiplied by all terms but itself, and becomes: [, 8]
        return res