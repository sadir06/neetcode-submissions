class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.current_path = []
        nums.sort()
        
        def backtracking(i):
            if i == len(nums):
                self.results.append(self.current_path[:]) # Make sure to create the shallow copy
                return # not gonna forget this this time

            
            self.current_path.append(nums[i])

            backtracking(i + 1)

            self.current_path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtracking(i + 1)
        backtracking(0)
        return self.results