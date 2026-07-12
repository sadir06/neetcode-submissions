class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []
        self.current_path = []

        def backtrack(open_count, close_count): # These will keep track of the open and closed bracket counts helping us track how many open and closed brackets we have right now
            if len(self.current_path) == 2 * n:
                self.results.append("".join(self.current_path)) 
                return # Never forgetting this again lol

            # Step 1: Place a (
            if open_count < n:
                self.current_path.append("(")
                open_count += 1
                backtrack(open_count, close_count)
                self.current_path.pop()
                open_count -= 1
            if close_count < open_count: # We are only allowed to close a bracket if there is an unmatched opening bracket
                self.current_path.append(")")
                close_count += 1
                backtrack(open_count, close_count)
                self.current_path.pop()
                close_count -= 1

        backtrack(0, 0)
        return self.results