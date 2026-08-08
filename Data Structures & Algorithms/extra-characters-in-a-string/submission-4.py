class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root # don't lose the root
        for c in word: # For each char in the word
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.flag = True # Set the flag at the last point
            
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.addWord(word)
        
        dp = {len(s):0}

        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1+ dfs(i + 1)
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]] # Move it along
                if curr.flag: # If at any point we reach the end of a word, update result
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res
        return dfs(0)