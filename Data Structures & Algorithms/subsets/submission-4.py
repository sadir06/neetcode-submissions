class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.current_path = []
        def backtrack(i):
            if i == len(nums):
                # We have reached the exit
                self.results.append(self.current_path[:])
                return
            self.current_path.append(nums[i])
            backtrack(i + 1)
            self.current_path.pop()
            backtrack(i + 1)

        backtrack(0)
        return self.results