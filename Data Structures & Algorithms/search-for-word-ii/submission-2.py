class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None # we use word here because we don't really care about the end of a word here, as we aren't checking if the ending exsits or not, prefixes are fine.

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.results = []
        self.root = TrieNode()
        self.directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        
        for word in words:
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word # At the end, store the word at the end

        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def backtrack(r, c, node):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited:
                return # Kill the path immediately

            if board[r][c] in node.children:
                node = node.children[board[r][c]] # this moves up node to the next node if it exists
            else:
                return # If there are no children, kill the search in this direction immediately, the word doesn't exist in this part of the grid
            if node.word:
                self.results.append(node.word) # This means that we have reached the end and there is a full word here, so we can add it to our results array
                node.word = None    
            
            visited.add((r, c))
            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                backtrack(nr, nc, node)
            visited.remove((r, c)) # Once all directions are exhausted for this letter, remove it from visited, as we will be moving onto exploring a new letter. 
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, self.root) # Try every single letter in the board
        return self.results
