class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.current_path = []
        self.used_set = set()
        def backtracking():
            if len(self.current_path) == len(nums): # We have found a valid combination
                self.result.append(self.current_path[:])
                return
            for num in nums:
                if num in self.used_set: # Skip this, as we already have this number and need to pick another number
                    continue
                self.current_path.append(num)
                self.used_set.add(num)
                backtracking() # We call this here because we want to explore more numbers after adding this value, and then we remove this value right after
                self.current_path.pop()
                self.used_set.remove(num)
        
        backtracking()
        return self.result