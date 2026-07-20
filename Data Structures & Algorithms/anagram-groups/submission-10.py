class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # Next instead of sorting every string, represent every string by the frequency of its characters, 2 strings are only identical if their frequencies are the same
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1 # For all words that have the same chars in some order, this number will be the same

            res[tuple(count)].append(word)
        return list(res.values())