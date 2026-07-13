class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char] 
        curr.flag = True # Set the final flag to True

    def search(self, word: str) -> bool:
        def backtracking(i, curr):
            if i == len(word):# We have processed all letters in the word
                return curr.flag # True or False

            char = word[i]
            if char == ".":
                for child in curr.children.values():
                    if backtracking(i + 1, child):
                        return True
                return False # Tried all the doors, and None worked
            else:
                if char not in curr.children:
                    return False
                return backtracking(i + 1, curr.children[char])
        return backtracking(0, self.root)