class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.results = []
        self.current_path = []
        self.current_sum = 0
        def backtrack(i, sum):
            if self.current_sum == target:
                # We have our exit condition, and we can return here
                self.results.append(self.current_path[:]) # We create a shallow copy here
                return # Exit the function
            if self.current_sum > target or i == len(nums):
                return # We are out of bounds, this is a dead end
            
            self.current_path.append(nums[i])
            self.current_sum += nums[i]
            backtrack(i, self.current_sum)
            self.current_sum -= nums[i]
            self.current_path.pop()
            backtrack(i + 1, self.current_sum)
        backtrack(0, self.current_sum)
        return self.results