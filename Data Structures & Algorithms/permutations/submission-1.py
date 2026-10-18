class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.used = set()
        self.current_path = []

        def dfs(i):
            if i == len(nums):
                self.result.append(self.current_path[:])
                return
            
            for num in nums:
                if num in self.used:
                    continue

                self.used.add(num)
                self.current_path.append(num)
                dfs(i + 1)
                self.used.remove(num)
                self.current_path.pop()



        dfs(0)
        return self.result