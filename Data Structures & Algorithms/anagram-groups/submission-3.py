class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Already initialised with full 0s
        for s in strs:
            sortedS = ''.join(sorted(s)) # sorted() returns a list of chars
            res[sortedS].append(s) # This works because a sorted anagram of another word is the same word
        return list(res.values()) # returns a list os lits, because res stores a list at it's value position