class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children: # If the letter doesn't alreayd exist, we create a new node at the value of the char
                curr.children[char] = TrieNode()
            curr = curr.children[char] # We always increment and go into the next room, which is the same as setting curr to the next room
        curr.end_of_word = True # This specific room has a True flag because this is where the word that was inserted ends

    def search(self, word: str) -> bool: # We have to return True or False if we find the word
        curr = self.root # We don't want to move self.root becaues it keeps an idea of where it is
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root # We don't want to move self.root becaues it keeps an idea of where it is
        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True