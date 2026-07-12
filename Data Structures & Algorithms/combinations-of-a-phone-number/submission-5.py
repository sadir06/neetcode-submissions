class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.results = []
        self.current_path = []
        digitToChar = { # I could NOT be bothered to type this out, so I just copied it from the solutions, because I knew we needed a mapping of the numbers to the letters
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def backtracking(i):
            if i == len(digits):
                self.results.append("".join(self.current_path))
                return
            if len(digitToChar[digits[i]]) == 4:
                n = 4
            else:
                n = 3
            for j in range(n): 
                self.current_path.append(digitToChar[digits[i]][j])
                backtracking(i + 1) 
                self.current_path.pop()

        backtracking(0)
        if self.results == [""]: # Essentially if we got an empty output, because we are adding "" into our list and they want us to return [], we just return that
            return []

        return self.results