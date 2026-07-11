class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.current_path = []
        self.current_sum = 0
        candidates.sort()

        def backtracking(i):
            if self.current_sum == target:
                self.result.append(self.current_path[:]) # Take a snapshot, this creates a shallow copy
                return
            if self.current_sum > target or i == len(candidates):
                return # This is unusable
            
            self.current_path.append(candidates[i])
            self.current_sum += candidates[i]
            backtracking(i + 1)
            self.current_path.pop()
            self.current_sum -= candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: # this checks for duplicates, it makes sure that we don't go out of bound, and if we do have duplicates, we move onto the next one and sprint past any identical clones, after having explroed them one time in the above loop
                i += 1
            backtracking(i + 1)

        backtracking(0)
        return self.result