from functools import reduce
import operator

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.results = []
        self.current_path = []


        def dfs(i):
            if i == len(nums): # If we have reached the end, we append it to results and return
                self.results.append(reduce(operator.xor, self.current_path, 0)) # If we have an empty list, which is a possible solution, we should return 0
                return 
            self.current_path.append(nums[i]) # Choosing the current number
            dfs(i + 1) # Moving onto the next number
            self.current_path.pop() # Not choosing the current number
            dfs(i + 1)
        dfs(0)
        return sum(self.results)