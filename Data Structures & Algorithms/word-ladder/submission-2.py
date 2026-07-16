from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        hashMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                part1 = word[:i]
                char = "*"
                part2 = word[i + 1:]
                word2 = part1 + char + part2
                hashMap[word2].append(word)

        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps # we have found the word

            for i in range(len(word)):
                part1 = word[:i]
                char = "*"
                part2 = word[i + 1:]
                pattern = part1 + char + part2
                output = hashMap[pattern]
                for wor in output: # lazy ahh coding
                    if wor not in visited:
                        visited.add(wor)
                        queue.append((wor, steps + 1))
        return 0 # If we hit this, no sequence exists. 
