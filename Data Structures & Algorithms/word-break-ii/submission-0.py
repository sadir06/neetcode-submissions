class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict) # We remove any duplicates, and get O(1) lookups
        self.result = []
        self.current_path = []
        def backtrack(i):
            if i == len(s): # We have reached the end of the word
                self.result.append(" ".join(self.current_path[:]))
                return

            for j in range(i, len(s)):
                w = s[i:j + 1] # Take this section of the word to search wordDict
                if w in wordDict: # The word NEET is in dict, but NEE isn't so it will select all of the correct words that are in the dict and only backtrack with them
                    self.current_path.append(w)
                    backtrack(j + 1) # Backtrack with this word in it
                    self.current_path.pop() # for the next iteration of j, we want the next letter and start our backtrack from there
            # If we reach the end of the loop without ever getting to the end (i.e. the word is just not in word dict, we will never entire i = len(s) and will just return eventually with an empty list which is correct)
                
            
        backtrack(0)
        return self.result