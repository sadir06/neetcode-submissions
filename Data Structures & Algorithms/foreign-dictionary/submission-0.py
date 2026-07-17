class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        hashMap = {char : set() for word in words for char in word} 
        
        for i in range(len(words) - 1): # We can use this to fill out the hashMap
            if len(words[i]) > len(words[i + 1]) and words[i].startswith(words[i + 1]): # This is a contradiction in the library and it is immediately broken
                return ""
            min_len = min(len(words[i]), len(words[i + 1]))
            for j in range(min_len): # We only loop for the common letters in both words
                if words[i][j] != words[i + 1][j]:
                    hashMap[words[i][j]].add(words[i + 1][j])
                    break # we have found the first different letter, the rest is irrelevant

        visit = {}
        results = []

        def dfs(char):
            if char in visit:
                if visit[char]:
                    return True
                else:
                    return False

            visit[char] = True
            for neighbor in hashMap[char]:
                if dfs(neighbor):
                    return True # We have found a cycle
            visit[char] = False # This line has become safe, set it back to safe
            results.append(char)
            return False

        for char in hashMap:
            if dfs(char):
                return "" # We have found an infinite cycle, this is not viable

        return "".join(results[::-1])