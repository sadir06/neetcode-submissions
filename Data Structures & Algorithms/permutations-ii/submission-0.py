class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.current_path = []
        count = {n : 0 for n in nums}
        for num in nums:
            count[num] += 1

        def dfs():
            if len(self.current_path) == len(nums):
                self.results.append(self.current_path[:])
                return
            
            for num in count: # For each value
                if count[num] > 0:# if the numbers count is greater than 0, meaning that it still has to be assigned
                    self.current_path.append(num) # Add that to the current path
                    count[num] -= 1 # Decrement it
                    dfs() # Continue to loop through, getting all the possible terms even with duplicates
                    count[num] += 1 # Incrememnt it, and remove it from the path, meaning that you choose it in another iteration. We will go to the next term and then next term will start the for loop from the start again, choosing the first value and decrementing it and so on and so forth. Very cool!
                    self.current_path.pop()
        dfs()
        return self.results