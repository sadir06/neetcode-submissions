class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.current_path = []
        def backtrack(i):
            if i == len(s):
                self.result.append(self.current_path[:])
                return

            for j in range(i, len(s)): # j is the index where our axe lands, we need contiguous blocks so we iterate from i to the end
                chunk = s[i:j+1] 
                if chunk == chunk[::-1]: # This is a palindrome
                    self.current_path.append(chunk) 
                    backtrack(j + 1)
                    self.current_path.pop()
        backtrack(0)
        return self.result